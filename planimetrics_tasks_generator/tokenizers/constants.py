PAD_TOKEN = "😀"
UNKNOWN_TOKEN = "😄"
START_TOKEN = "🤣"
END_TOKEN = "😎"

DEFAULT_TOKENS = (PAD_TOKEN, START_TOKEN, END_TOKEN, UNKNOWN_TOKEN)
PAD_IDX, START_IDX, END_IDX, UNKNOWN_IDX = [i for i, _ in enumerate(DEFAULT_TOKENS)]
