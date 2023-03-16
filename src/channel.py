from googleapiclient.discovery import build
import os


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        # self.title = title
        # self.video_count = video_count
        # self.url = url

    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        return self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    # def to_json(self, filename: str):
    # json_object = json.dumps({
    #  "id": self.channel_id,
    # "title": self.title,
    # "video_count": self.video_count,
    # "url": self.url
    # }, indent=4)

    # with open(filename, "w") as outfile:
    #   outfile.write(json_object)
