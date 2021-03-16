#выбор из фильра по задаче
from yandex_tracker_client import TrackerClient

client = TrackerClient(token='AgAEA7qi-OYuAAb4wbjTn3nDNUCMoGrvbqro1aA', org_id='27626')
# Здесь <token> — ваш OAuth-токен, а <org_id> — идентификатор организации.

issues = client.issues.find(
    ' Queue: Претензии  AND Assignee: group( value: Developers ) AND Status: "Техническое моделирование", Разработка , Тестирование , "Тестирование завершено" , "Код ревью" , RC , "Готово к релизу" ')
# print ([issue.key for issue in issues])

for issue in issues:
    print(issue.key)
    print(issue.summary)  # Название задачи.
    # print(issue.updatedAt)

    transitions = issue.transitions.get_all()
    for transition in transitions:
        print(transition)
        print(issue.updatedAt)
    print("")
