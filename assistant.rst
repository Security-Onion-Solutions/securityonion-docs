.. _onionai:

Onion AI
========

.. note::

    This is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonion.com/pro for more information about purchasing a :ref:`pro` license.

The Onion AI Assistant is your personal AI helper designed to assist you with a variety of tasks and provide information on demand. Several tools have been made available as you interact with the assistant so it can access up-to-date information and resources.

Credits
-------

The Security Onion Pro license includes an initial amount of credits to get started. For long term usage planning contact your Security Onion account representative. They will assist with estimating credit usage rates as well as the provisioning of additional credits. Credits are consumed based on the number of tokens used in the conversation including user input, assistant output, and tool usage. Your organization's balance can be viewed at the top right of the assistant page or on the management page under Administration --> AI Metrics.

Available Tools
---------------

The assistant currently runs in the cloud. In order to reference local information, SOC makes the following tools available to the assistant:

 - query_events: This read-only tool allows the assistant to query security events from your local Security Onion instance similar to how you would use the :ref:`hunt` page.
 - get_playbooks: When the assistant uses this read-only tool, SOC will gather the playbooks, execute their queries, and return all the data ready for analysis.
 - ack_alerts: The assistant can use this tool to query and acknowledge :ref:`alerts` in your local Security Onion instance.
 - escalate_alerts: Similar to the ack tool, this tool allows the assistant to query for alerts and escalate them to a new case.

Permissions
~~~~~~~~~~~

When the assistant requests any of these tools, the user will be prompted to approve or reject the usage. Approval will have the tool run and the result entered into the conversation followed by a response from the AI. Rejection will notify the assistant and allow it to respond.

Auto Approve Read-Only Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following read-only tools can be used by the assistant without requiring explicit user approval:

 - query_events
 - get_playbooks

By default, permission must be granted for each tool request. However, users can enable auto-approval for read-only tools by toggling the slider in the Options dropdown at the top of the assistant page. With the option enabled, read-only tools will auto approve, while tools that modify data (acknowledge and escalate alerts) will still request explicit user approval.

.. note::

    Conversation data is stored locally and not used to train any models. However, be cautious about sharing sensitive or personal information during your interactions as others in your organization may have access to the conversation history.

Customizing the System Prompt
-----------------------------

The system prompt sets the behavior and context for the AI assistant. Users can customize this prompt to tailor the assistant's responses to their specific needs, such as describing network resources, environments, or workflows. The prompt is included in every session and can be modified at any time on the Administration --> Configuration page under soc --> config --> server --> modules --> assistant --> systemPromptAddendum.

Your system prompt addendum will be added after Security Onion's default system prompt.

.. note::

		Be cautious when customizing the system prompt, as it can significantly influence the assistant's behavior and responses. A longer prompt will also use more credits.

Management
----------

Superusers can manage token usage and view conversation history for all users from the management page under Administration --> AI Metrics. This page provides usage statistics for a given date range. The page starts with a table of usage by user. Clicking a user's binoculars icon on the right hand side will show any sessions the user interacted with during the selected date range, even deleted sessions. Clicking on a session's binoculars icon will show the full conversation.
