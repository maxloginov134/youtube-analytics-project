class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        # self.title = title
        # self.video_count = video_count
        # self.url = url

    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        return self.channel_id

    # def to_json(self, filename: str):
    # json_object = json.dumps({
    #  "id": self.channel_id,
    # "title": self.title,
    # "video_count": self.video_count,
    # "url": self.url
    # }, indent=4)

    # with open(filename, "w") as outfile:
    #   outfile.write(json_object)
