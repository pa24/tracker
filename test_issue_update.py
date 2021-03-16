from yandex_tracker_client import TrackerClient

client = TrackerClient(token='AgAEA7qi-OYuAAb4wbjTn3nDNUCMoGrvbqro1aA', org_id='27626')
# Здесь <token> — ваш OAuth-токен, а <org_id> — идентификатор организации.
issue = client.issues['CLAIM-15718']
print(issue.updatedAt)
