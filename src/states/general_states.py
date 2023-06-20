from aiogram.dispatcher.filters.state import State, StatesGroup

class VerificationAccountState(StatesGroup): 
    StartVerification = State()
    WaitPassword = State()

class SpectateGitHubState(StatesGroup):
    StartSpectate = State()

class SpectateTwitchState(StatesGroup):
    StartSpectate = State()

class SpectateVKState(StatesGroup):
    StartSpectate = State()

class SpectateDiscordState(StatesGroup):
    StartSpectate = State()

class SpectateTelegramState(StatesGroup):
    StartSpectate = State()

