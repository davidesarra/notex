class NotexError(Exception):
    pass


class ConversionError(NotexError):
    pass


class MissingTitle(ConversionError):
    pass


class NonUniqueTitle(ConversionError):
    pass


class FileNotFound(NotexError):
    pass
