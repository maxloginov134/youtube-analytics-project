

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, title: str, video_count: int, url: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = title
        self.video_count = video_count
        self.url = url

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pass
