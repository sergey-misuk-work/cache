from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import date
from uuid import uuid4
from typing import List


@dataclass_json
@dataclass
class DailyResponse:
    chats_from_autosuggest_count: int
    chats_from_user_count: int
    chats_from_visitor_count: int
    conversation_count: int
    date: date
    missed_chat_count: int
    user_message_count: int
    visitor_message_count: int
    visitors_affected_by_chat_count: int
    visitors_autosuggested_count: int
    visitors_with_chat_count: int
    visitors_with_conversation_count: int


@dataclass_json
@dataclass
class APIResponse:
    by_date: List[DailyResponse]
    end_date: date
    room_id: uuid4
    start_date: date
    total_chats_from_autosuggest_count: int
    total_chats_from_user_count: int
    total_chats_from_visitor_count: int
    total_conversation_count: int
    total_missed_chat_count: int
    total_user_message_count: int
    total_visitor_message_count: int
    total_visitors_affected_by_chat_count: int
    total_visitors_autosuggested_count: int
    total_visitors_with_chat_count: int
    total_visitors_with_conversation_count: int
