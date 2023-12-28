# GITHUB configuration
GIT_HUB_TOKEN = 'your token'
HEADERS = {'Authorization': f'Bearer {GIT_HUB_TOKEN}'}
# Enter your project pulls url, like below, but instead of +project dir+ smth like /project/test/,
PRS_URL = 'https://api.github.com/repos/+project dir+/pulls'

# devs in format: {'github_nick_name': '@telegram_nick_name'}
DEVELOPERS = {
    'no_reviewers': 'Не указаны reviewers, арест на 15 суток 👮🏻♥️',
    'no_assignee': 'Не указан assignee, лишение прав 👮🏻♥️'
}

# GITLAB configuration
headers = {'PRIVATE-TOKEN': 'your token'}
# Enter your project number
project_number = 11111111
opened_merge_requests_url = f'https://gitlab.com/api/v4/projects/{project_number}/merge_requests?state=opened'
merge_requests_url = f'https://gitlab.com/api/v4/projects/{project_number}/merge_requests/'

# devs in format: {'gitlab_nick_name': '@telegram_nick_name'}
developers = {
    'none': '❌ Не указан assignee, штраф 1000 золотых',
    'noSuchUser': '💢🤦‍♀ Не поняла, это кто?'
}

# Common
animation_url = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDhlZ3IwenJjNThybGFkbnN2NW56ODJ6YWZkcXVlcHRpdHk0ZTFyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10M8Yr4WKJK63e/giphy.gif'
delay_in_seconds = 60
required_approves_count = 3
work_days_count = 5
work_days = list(range(work_days_count))

# Create bots for production telegram chat and for test chat:
# change to switch between Copy bot and MrMother bot:
debug_mode_is_on = False
sound_is_on = True

# enter your copy bot token for testing
api_copy_bot_token = 'api_copy_bot_token'
# enter your production bot token
api_mr_mother_bot_token = 'api_mr_mother_bot_token'
# enter test chat id
dev_copy_chat_id = -1111111111111
# enter production chat id
dev_ios_internal_chat_id = -1111111111111

api_bot_token = api_copy_bot_token if debug_mode_is_on else api_mr_mother_bot_token
dev_chat_id = dev_copy_chat_id if debug_mode_is_on else dev_ios_internal_chat_id

# Enter pr messages schedule time
schedule = {
    '10:00',
    '13:00',
    '15:30',
    '17:30',
}

# Enter everyday team daily call time notification
daily_schedule = {
    0: '16:00',
    1: '16:00',
    2: '16:00',
    3: '16:00',
    4: '16:00'
}