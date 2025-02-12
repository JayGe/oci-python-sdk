# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OdaInstance(object):
    """
    Description of `OdaServiceInstance` object.
    """

    #: A constant which can be used with the shape_name property of a OdaInstance.
    #: This constant has a value of "DEVELOPMENT"
    SHAPE_NAME_DEVELOPMENT = "DEVELOPMENT"

    #: A constant which can be used with the shape_name property of a OdaInstance.
    #: This constant has a value of "PRODUCTION"
    SHAPE_NAME_PRODUCTION = "PRODUCTION"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OdaInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "DELETE_PENDING"
    LIFECYCLE_SUB_STATE_DELETE_PENDING = "DELETE_PENDING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "PURGING"
    LIFECYCLE_SUB_STATE_PURGING = "PURGING"

    #: A constant which can be used with the lifecycle_sub_state property of a OdaInstance.
    #: This constant has a value of "QUEUED"
    LIFECYCLE_SUB_STATE_QUEUED = "QUEUED"

    def __init__(self, **kwargs):
        """
        Initializes a new OdaInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OdaInstance.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OdaInstance.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OdaInstance.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OdaInstance.
        :type compartment_id: str

        :param shape_name:
            The value to assign to the shape_name property of this OdaInstance.
            Allowed values for this property are: "DEVELOPMENT", "PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shape_name: str

        :param web_app_url:
            The value to assign to the web_app_url property of this OdaInstance.
        :type web_app_url: str

        :param connector_url:
            The value to assign to the connector_url property of this OdaInstance.
        :type connector_url: str

        :param time_created:
            The value to assign to the time_created property of this OdaInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OdaInstance.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OdaInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_sub_state:
            The value to assign to the lifecycle_sub_state property of this OdaInstance.
            Allowed values for this property are: "DELETE_PENDING", "PURGING", "QUEUED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_sub_state: str

        :param state_message:
            The value to assign to the state_message property of this OdaInstance.
        :type state_message: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OdaInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OdaInstance.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'shape_name': 'str',
            'web_app_url': 'str',
            'connector_url': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_sub_state': 'str',
            'state_message': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'shape_name': 'shapeName',
            'web_app_url': 'webAppUrl',
            'connector_url': 'connectorUrl',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_sub_state': 'lifecycleSubState',
            'state_message': 'stateMessage',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._shape_name = None
        self._web_app_url = None
        self._connector_url = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_sub_state = None
        self._state_message = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OdaInstance.
        Unique immutable identifier that was assigned when the instance was created.


        :return: The id of this OdaInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OdaInstance.
        Unique immutable identifier that was assigned when the instance was created.


        :param id: The id of this OdaInstance.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this OdaInstance.
        User-defined name for the Digital Assistant instance. Avoid entering confidential information.
        You can change this value.


        :return: The display_name of this OdaInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OdaInstance.
        User-defined name for the Digital Assistant instance. Avoid entering confidential information.
        You can change this value.


        :param display_name: The display_name of this OdaInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this OdaInstance.
        Description of the Digital Assistant instance.


        :return: The description of this OdaInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OdaInstance.
        Description of the Digital Assistant instance.


        :param description: The description of this OdaInstance.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OdaInstance.
        Identifier of the compartment that the instance belongs to.


        :return: The compartment_id of this OdaInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OdaInstance.
        Identifier of the compartment that the instance belongs to.


        :param compartment_id: The compartment_id of this OdaInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this OdaInstance.
        Shape or size of the instance.

        Allowed values for this property are: "DEVELOPMENT", "PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shape_name of this OdaInstance.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this OdaInstance.
        Shape or size of the instance.


        :param shape_name: The shape_name of this OdaInstance.
        :type: str
        """
        allowed_values = ["DEVELOPMENT", "PRODUCTION"]
        if not value_allowed_none_or_none_sentinel(shape_name, allowed_values):
            shape_name = 'UNKNOWN_ENUM_VALUE'
        self._shape_name = shape_name

    @property
    def web_app_url(self):
        """
        Gets the web_app_url of this OdaInstance.
        URL for the Digital Assistant web application that's associated with the instance.


        :return: The web_app_url of this OdaInstance.
        :rtype: str
        """
        return self._web_app_url

    @web_app_url.setter
    def web_app_url(self, web_app_url):
        """
        Sets the web_app_url of this OdaInstance.
        URL for the Digital Assistant web application that's associated with the instance.


        :param web_app_url: The web_app_url of this OdaInstance.
        :type: str
        """
        self._web_app_url = web_app_url

    @property
    def connector_url(self):
        """
        Gets the connector_url of this OdaInstance.
        URL for the connector's endpoint.


        :return: The connector_url of this OdaInstance.
        :rtype: str
        """
        return self._connector_url

    @connector_url.setter
    def connector_url(self, connector_url):
        """
        Sets the connector_url of this OdaInstance.
        URL for the connector's endpoint.


        :param connector_url: The connector_url of this OdaInstance.
        :type: str
        """
        self._connector_url = connector_url

    @property
    def time_created(self):
        """
        Gets the time_created of this OdaInstance.
        When the Digital Assistant instance was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this OdaInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OdaInstance.
        When the Digital Assistant instance was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this OdaInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OdaInstance.
        When the Digital Assistance instance was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this OdaInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OdaInstance.
        When the Digital Assistance instance was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this OdaInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OdaInstance.
        The current state of the Digital Assistant instance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OdaInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OdaInstance.
        The current state of the Digital Assistant instance.


        :param lifecycle_state: The lifecycle_state of this OdaInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_sub_state(self):
        """
        Gets the lifecycle_sub_state of this OdaInstance.
        The current sub-state of the Digital Assistant instance.

        Allowed values for this property are: "DELETE_PENDING", "PURGING", "QUEUED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_sub_state of this OdaInstance.
        :rtype: str
        """
        return self._lifecycle_sub_state

    @lifecycle_sub_state.setter
    def lifecycle_sub_state(self, lifecycle_sub_state):
        """
        Sets the lifecycle_sub_state of this OdaInstance.
        The current sub-state of the Digital Assistant instance.


        :param lifecycle_sub_state: The lifecycle_sub_state of this OdaInstance.
        :type: str
        """
        allowed_values = ["DELETE_PENDING", "PURGING", "QUEUED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_sub_state, allowed_values):
            lifecycle_sub_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_sub_state = lifecycle_sub_state

    @property
    def state_message(self):
        """
        Gets the state_message of this OdaInstance.
        A message that describes the current state in more detail.
        For example, actionable information about an instance that's in the `FAILED` state.


        :return: The state_message of this OdaInstance.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this OdaInstance.
        A message that describes the current state in more detail.
        For example, actionable information about an instance that's in the `FAILED` state.


        :param state_message: The state_message of this OdaInstance.
        :type: str
        """
        self._state_message = state_message

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OdaInstance.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OdaInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OdaInstance.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OdaInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OdaInstance.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OdaInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OdaInstance.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OdaInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
