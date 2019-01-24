from reminder import Reminder, EmailReminder, PopupReminder
from serializers.base_serializer import BaseSerializer


class ReminderSerializer(BaseSerializer):
    type_ = Reminder

    def __init__(self, reminder):
        super().__init__(reminder)

    @staticmethod
    def to_json(reminder):
        return {
            'method': reminder.method,
            'minutes': reminder.minutes_before_start
        }

    @staticmethod
    def to_object(json_reminder):
        super().assure_dict(json_reminder)

        method = json_reminder['method']
        if method == 'email':
            return EmailReminder(int(json_reminder['minutes_before_start']))
        elif method == 'popup':
            return PopupReminder(int(json_reminder['minutes_before_start']))
        else:
            raise ValueError('Unexpected method "{}" for a reminder.'.format(method))
