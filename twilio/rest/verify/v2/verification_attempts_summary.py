r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class VerificationAttemptsSummaryInstance(InstanceResource):
    class Channels(object):
        SMS = "sms"
        CALL = "call"
        EMAIL = "email"
        WHATSAPP = "whatsapp"

    """
    :ivar total_attempts: Total of attempts made according to the provided filters
    :ivar total_converted: Total of  attempts made that were confirmed by the end user, according to the provided filters.
    :ivar total_unconverted: Total of attempts made that were not confirmed by the end user, according to the provided filters.
    :ivar conversion_rate_percentage: Percentage of the confirmed messages over the total, defined by (total_converted/total_attempts)*100. 
    :ivar url: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.total_attempts: Optional[int] = deserialize.integer(
            payload.get("total_attempts")
        )
        self.total_converted: Optional[int] = deserialize.integer(
            payload.get("total_converted")
        )
        self.total_unconverted: Optional[int] = deserialize.integer(
            payload.get("total_unconverted")
        )
        self.conversion_rate_percentage: Optional[float] = deserialize.decimal(
            payload.get("conversion_rate_percentage")
        )
        self.url: Optional[str] = payload.get("url")

        self._context: Optional[VerificationAttemptsSummaryContext] = None

    @property
    def _proxy(self) -> "VerificationAttemptsSummaryContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: VerificationAttemptsSummaryContext for this VerificationAttemptsSummaryInstance
        """
        if self._context is None:
            self._context = VerificationAttemptsSummaryContext(
                self._version,
            )
        return self._context

    def fetch(
        self,
        verify_service_sid: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union[
            "VerificationAttemptsSummaryInstance.Channels", object
        ] = values.unset,
        destination_prefix: Union[str, object] = values.unset,
    ) -> "VerificationAttemptsSummaryInstance":
        """
        Fetch the VerificationAttemptsSummaryInstance

        :param verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
        :param date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param country: Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
        :param channel: Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are `SMS`, `CALL` and `WHATSAPP`
        :param destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.

        :returns: The fetched VerificationAttemptsSummaryInstance
        """
        return self._proxy.fetch(
            verify_service_sid=verify_service_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            country=country,
            channel=channel,
            destination_prefix=destination_prefix,
        )

    async def fetch_async(
        self,
        verify_service_sid: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union[
            "VerificationAttemptsSummaryInstance.Channels", object
        ] = values.unset,
        destination_prefix: Union[str, object] = values.unset,
    ) -> "VerificationAttemptsSummaryInstance":
        """
        Asynchronous coroutine to fetch the VerificationAttemptsSummaryInstance

        :param verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
        :param date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param country: Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
        :param channel: Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are `SMS`, `CALL` and `WHATSAPP`
        :param destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.

        :returns: The fetched VerificationAttemptsSummaryInstance
        """
        return await self._proxy.fetch_async(
            verify_service_sid=verify_service_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            country=country,
            channel=channel,
            destination_prefix=destination_prefix,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Verify.V2.VerificationAttemptsSummaryInstance>"


class VerificationAttemptsSummaryContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the VerificationAttemptsSummaryContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Attempts/Summary"

    def fetch(
        self,
        verify_service_sid: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union[
            "VerificationAttemptsSummaryInstance.Channels", object
        ] = values.unset,
        destination_prefix: Union[str, object] = values.unset,
    ) -> VerificationAttemptsSummaryInstance:
        """
        Fetch the VerificationAttemptsSummaryInstance

        :param verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
        :param date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param country: Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
        :param channel: Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are `SMS`, `CALL` and `WHATSAPP`
        :param destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.

        :returns: The fetched VerificationAttemptsSummaryInstance
        """

        data = values.of(
            {
                "VerifyServiceSid": verify_service_sid,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "Country": country,
                "Channel": channel,
                "DestinationPrefix": destination_prefix,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return VerificationAttemptsSummaryInstance(
            self._version,
            payload,
        )

    async def fetch_async(
        self,
        verify_service_sid: Union[str, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union[
            "VerificationAttemptsSummaryInstance.Channels", object
        ] = values.unset,
        destination_prefix: Union[str, object] = values.unset,
    ) -> VerificationAttemptsSummaryInstance:
        """
        Asynchronous coroutine to fetch the VerificationAttemptsSummaryInstance

        :param verify_service_sid: Filter used to consider only Verification Attempts of the given verify service on the summary aggregation.
        :param date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param country: Filter used to consider only Verification Attempts sent to the specified destination country on the summary aggregation.
        :param channel: Filter Verification Attempts considered on the summary aggregation by communication channel. Valid values are `SMS`, `CALL` and `WHATSAPP`
        :param destination_prefix: Filter the Verification Attempts considered on the summary aggregation by Destination prefix. It is the prefix of a phone number in E.164 format.

        :returns: The fetched VerificationAttemptsSummaryInstance
        """

        data = values.of(
            {
                "VerifyServiceSid": verify_service_sid,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "Country": country,
                "Channel": channel,
                "DestinationPrefix": destination_prefix,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return VerificationAttemptsSummaryInstance(
            self._version,
            payload,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Verify.V2.VerificationAttemptsSummaryContext>"


class VerificationAttemptsSummaryList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the VerificationAttemptsSummaryList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> VerificationAttemptsSummaryContext:
        """
        Constructs a VerificationAttemptsSummaryContext

        """
        return VerificationAttemptsSummaryContext(self._version)

    def __call__(self) -> VerificationAttemptsSummaryContext:
        """
        Constructs a VerificationAttemptsSummaryContext

        """
        return VerificationAttemptsSummaryContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.VerificationAttemptsSummaryList>"
