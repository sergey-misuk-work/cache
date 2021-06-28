from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import date, datetime
from uuid import uuid4
from typing import List


@dataclass_json
@dataclass
class DailyResponse:
    date: date
    conversation_count: int
    missed_chat_count: int
    visitors_with_conversation_count: int


@dataclass_json
@dataclass
class TotalResponse:
    conversation_count: int
    missed_chat_count: int
    visitors_with_conversation_count: int


@dataclass_json
@dataclass
class DailyResponseExternal:
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

    def to_daily_response(self) -> DailyResponse:
        return DailyResponse(
            # TODO: find out why it's not parsed into date automatically
            date=self.date if isinstance(self.date, date) else datetime.strptime(self.date, '%Y-%m-%d').date(),
            conversation_count=self.conversation_count,
            missed_chat_count=self.missed_chat_count,
            visitors_with_conversation_count=self.visitors_with_conversation_count,
        )


@dataclass_json
@dataclass
class TotalResponseExternal:
    by_date: List[DailyResponseExternal]
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

    def to_total_response(self) -> TotalResponse:
        return TotalResponse(
            conversation_count=self.total_conversation_count,
            missed_chat_count=self.total_missed_chat_count,
            visitors_with_conversation_count=self.total_visitors_with_conversation_count,
        )
