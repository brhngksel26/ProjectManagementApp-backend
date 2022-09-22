import aiohttp
from project_management.model.application import Application


class Slack:

    async def send_message(self, params):
        print(params)
        data = f'{{"text": "{str(params)}"}}'

        url = await self._get_webhooks()

        async with aiohttp.ClientSession() as client:
            async with client.post(url, data=data) as session:
                response = await session.read()

        return {"status_message": response.decode("utf-8")}

    async def _get_webhooks(self):
        if app_info := Application.objects.filter(name="Slack").first():
            return app_info["token"]
        else:
            raise "Slack App Not Found"