from operator import attrgetter
from pytest import fixture
from rest_framework.test import APIRequestFactory
from typing import List, Dict
from cache.data import TotalResponseExternal, SingleDay, TotalResponse, DailyResponse


@fixture(scope='session')
def raw_response_external() -> str:
    return """{
    "by_date": [
        {
            "chats_from_autosuggest_count": 141,
            "chats_from_user_count": 0,
            "chats_from_visitor_count": 4,
            "conversation_count": 9,
            "date": "2017-06-12",
            "missed_chat_count": 1,
            "user_message_count": 68,
            "visitor_message_count": 61,
            "visitors_affected_by_chat_count": 139,
            "visitors_autosuggested_count": 135,
            "visitors_with_chat_count": 13,
            "visitors_with_conversation_count": 9
        },
        {
            "chats_from_autosuggest_count": 168,
            "chats_from_user_count": 0,
            "chats_from_visitor_count": 2,
            "conversation_count": 12,
            "date": "2017-06-13",
            "missed_chat_count": 1,
            "user_message_count": 85,
            "visitor_message_count": 95,
            "visitors_affected_by_chat_count": 160,
            "visitors_autosuggested_count": 160,
            "visitors_with_chat_count": 13,
            "visitors_with_conversation_count": 11
        },
        {
            "chats_from_autosuggest_count": 117,
            "chats_from_user_count": 0,
            "chats_from_visitor_count": 4,
            "conversation_count": 9,
            "date": "2017-06-14",
            "missed_chat_count": 1,
            "user_message_count": 147,
            "visitor_message_count": 130,
            "visitors_affected_by_chat_count": 111,
            "visitors_autosuggested_count": 107,
            "visitors_with_chat_count": 13,
            "visitors_with_conversation_count": 8
        },
        {
            "chats_from_autosuggest_count": 84,
            "chats_from_user_count": 2,
            "chats_from_visitor_count": 3,
            "conversation_count": 9,
            "date": "2017-06-15",
            "missed_chat_count": 0,
            "user_message_count": 45,
            "visitor_message_count": 38,
            "visitors_affected_by_chat_count": 87,
            "visitors_autosuggested_count": 82,
            "visitors_with_chat_count": 13,
            "visitors_with_conversation_count": 9
        }
    ],
    "end_date": "2017-06-15",
    "room_id": "84e0fefa-5675-11e7-a349-00163efdd8db",
    "start_date": "2017-06-12",
    "total_chats_from_autosuggest_count": 510,
    "total_chats_from_user_count": 2,
    "total_chats_from_visitor_count": 13,
    "total_conversation_count": 39,
    "total_missed_chat_count": 3,
    "total_user_message_count": 345,
    "total_visitor_message_count": 324,
    "total_visitors_affected_by_chat_count": 497,
    "total_visitors_autosuggested_count": 484,
    "total_visitors_with_chat_count": 52,
    "total_visitors_with_conversation_count": 37
}"""


@fixture(scope="session")
def response_external(raw_response_external: str) -> TotalResponseExternal:
    return TotalResponseExternal.from_json(raw_response_external)


@fixture(scope="session")
def daily_data(response_external: TotalResponseExternal) -> List[SingleDay]:
    return [datum.to_single_day() for datum in response_external.by_date]


@fixture(scope="session")
def daily_response(daily_data: List[SingleDay]) -> DailyResponse:
    return DailyResponse(
        count=len(daily_data),
        data=daily_data,
    ).to_dict()


@fixture(scope="session")
def total_data(daily_data: List[SingleDay]) -> TotalResponse:
    return TotalResponse(
        conversation_count=sum(map(attrgetter('conversation_count'), daily_data)),
        missed_chat_count=sum(map(attrgetter('missed_chat_count'), daily_data)),
        visitors_with_conversation_count=sum(map(attrgetter('visitors_with_conversation_count'), daily_data)),
    )


@fixture(scope="session")
def total_response(total_data: TotalResponse) -> Dict:
    return total_data.to_dict()


@fixture
def request_factory():
    return APIRequestFactory()
