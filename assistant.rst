.. _onionai:

Onion AI
========

.. note::

    This is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonion.com/pro for more information about purchasing a :ref:`pro` license.

The Onion AI Assistant is your personal AI helper designed to assist you with a variety of tasks and provide information on demand. We support accessing LLMs from a variety of sources. Several tools help you interact with the assistant so it can access up-to-date information and resources.

Adapters
--------

There are a variety of adapters available to connect to different LLM providers. When configuring an adapter, you're instructing SOC how to connect to an LLM provider. You configure the models seperately in :ref:`available-models` and tell each model which adapter to use. This allows you to connect to multiple providers at the same time and choose which models you want to use from each provider. The available adapters are:

 - **SOAI**: The Security Onion AI adapter connects to our own hosted gateway and provides access to a variety of models. This is the default adapter, and is hosted in the cloud with an allotted number of credits per Security Onion Pro licensed grids.
 - **Gemini**: Google's Gemini models can be accessed through this adapter. You can connect through either the Gemini Developer API or the Vertex API. These models are hosted in Google's cloud and require the use of your own Google Cloud key, or Gemini API key.
 - **OpenAI Responses**: This adapter can connect to the newest OpenAI compatible APIs that support the Responses protocol. This adapter allows Security Onion grids to connect to locally-hosted LLMs.
 - **OpenAI Chat**: This adapter can connect to any OpenAI Chat compatible APIs, an older protocol still supported by many AI providers. This adapter allows Security Onion grids to connect to locally-hosted LLMs.

Most features are supported across all adapters, but capabilities may change depending on the model or provider you connect to. Credits are unique to SOAI, it's the only adapter that responds with a credit balance. Multiple adapters can be configured at the same time.

Configuration
~~~~~~~~~~~~~

A fresh install will come with the SOAI adapter pre-configured and ready to use. To connect to other providers or modify the SOAI adapter, go to Administration --> Configuration page, be sure "Show advanced settings" is turned on in the Options at the top of the page, and check under soc --> config --> server --> modules --> assistant --> adapters. Here you can add as many adapters as you need. Each adapter defines how to connect to a provider. Different adapters have different configuration requirements. Every adapter needs a unique name, the protocol it uses, and a Health Timeout measured in seconds. Below is a table of which fields are required for which adapters:

.. list-table::
    :header-rows: 1
    :name: assistant-config-table

    * - 
      - Adapter Name
      - Protocol
      - API Url
      - API Key
      - Service Account JSON
      - Service Account Location
      - Health Timeout Seconds
    * - SOAI
      - R
      - R
      - R
      - --
      - --
      - --
      - R
    * - Gemini
      - R
      - R
      - --
      - O
      - O
      - O
      - R
    * - OpenAI Responses
      - R
      - R
      - R
      - O
      - --
      - --
      - R
    * - OpenAI Chat
      - R
      - R
      - R
      - O
      - --
      - --
      - R
R = Required, O = Optional, -- = Not Used

SOAI
~~~~

This adapter should not require any configuration, aside from the API Url, which will be different for Security Onion Pro customers located in different regions. If your license is setup to use an alternate cloud region this information will be included with the Security Onion license key. If it is not specified then use the default API url.

Any additionally supplied fields are ignored. Generally at most one instance of this adapter should be configured at a time.

Using models over this adapter will cost credits. Contact your account representative for more information.

Gemini
~~~~~~~

Security Onion supports connecting to Google's Gemini models through either the Gemini Developer API or the Vertex API.

To connect over the Gemini Developer API, you will need to generate an API Key in the Google Cloud Console or Google AI Studio, and provide it in the API Key field. To connect over the Vertex API, you will need to create a Service Account with the appropriate permissions for the models you would like to access, generate a JSON key for that account, paste the JSON into the Service Account JSON field, and you must also specify the Service Account Location. Some Gemini models may only be available in certain locations, such as ``global``. The API Url field is not used for Gemini connections.

If an API Key and Service Account JSON + Service Account Location are both provided, SOC will attempt to connect using the Service Account and the API Key will be ignored.

This adapter will not use any credits from your Security Onion Pro license, but Google will charge you based on their pricing. Security Onion Solutions, LLC does not provide support for Google Gemini, aside from assisting with the adapter configuration referenced on this page.

OpenAI Responses
~~~~~~~~~~~~~~~~

The *OpenAI Responses* adapter can connect to the newest OpenAI compatible APIs that support the Responses protocol. To connect, you will need to provide an API Url. The API Url should be the base url for the provider you are connecting to, for example ``https://api.openai.com/v1/``. An API Key may or may not be required depending on the provider you are connecting to. If you're unsure if your provider supports the Responses protocol, check with their support or try connecting with this adapter. If it doesn't work, you can try the *OpenAI Chat* adapter which supports an older protocol that is still widely used.

OpenAI Chat
~~~~~~~~~~~

The *OpenAI Chat* adapter can connect to any OpenAI compatible API that supports the Chat protocol. To connect, you will need to provide an API Url. The API Url should be the base url for the provider you are connecting to, for example ``https://api.openai.com/v1/``. An API Key may or may not be required depending on the provider you are connecting to.

.. _available-models:
Available Models
----------------

In order to control what models are available inside SOC, individual models must be configured. To configure a model, go to the Administration --> Configuration page, be sure "Show advanced settings" is turned on in the Options at the top of the page, and check under soc --> config --> server --> client --> assistant --> availableModels. Here you can add as many models as you need. Each model needs a unique name, the adapter it uses, and a model identifier which tells the adapter which model to connect to on the provider.

.. note::

    If a provider offers models that aren't listed in availableModels, they will not be accessible within SOC.

Credits
-------

The Security Onion Pro license includes an initial amount of credits to get started. For long term usage planning contact your Security Onion account representative. They will assist with estimating credit usage rates as well as the provisioning of additional credits. Credits are consumed based on the number of tokens used in the conversation including user input, assistant output, and tool usage. Your organization's balance can be viewed at the top right of the assistant page or on the management page under Administration --> AI Metrics.

Local Model Considerations
--------------------------

Security Onion now supports local models through any OpenAI-compatible endpoint. Because the assistant relies on large context windows, the minimum recommended context length is 128k tokens. The following open-source models have been tested with OnionAI:

- **GPT OSS 120B** -- (US) Fast inference but limited to a 128k context window. Accuracy is fair.
- **Kimi 2.5** -- (China) A capable model with average accuracy and a 256k context window sufficient for most tasks. Note that this model requires significant VRAM to maintain performance.
- **GLM 5** -- (China) Average accuracy with a 200k context window.
- **Qwen 3.5** -- (China) Average accuracy with a 200k context window.

.. note::

    Local models will not match the performance of proprietary foundational models such as those from Anthropic, Google, or OpenAI.

Hosting Local Models
--------------------

Hosting your own models requires powerful and expensive hardware. For beginners we recommend using a tool such as LM Studio. **You need at least 96GB of VRAM** to host your own models locally. The speed and accuracy of OnionAI when hosted locally is based on the hardware that you are using. For the most accurate results we recommend using credits with OnionAI.

Available Tools
---------------

The assistant currently runs in the cloud. In order to reference local information, SOC makes the following tools available to the assistant:

 - **query_events**: This read-only tool allows the assistant to query security events from your local Security Onion instance similar to how you would use the :ref:`hunt` page.
 - **query_cases**: This tool allows the assistant to query cases from your local Security Onion instance similar to how you would use the :ref:`cases` page.
 - **query_detections**: This tool allows the assistant to query detections from your local Security Onion instance similar to how you would use the :ref:`detections` page.
 - **get_playbooks**: When the assistant uses this read-only tool, SOC will gather the playbooks, execute their queries, and return all the data ready for analysis. This tool is read-only.
 - **ack_alerts**: The assistant can use this tool to query and acknowledge :ref:`alerts` in your local Security Onion instance.
 - **escalate_alerts**: Similar to the ack tool, this tool allows the assistant to query for alerts and escalate them to a new case.
 - **create_detection**: The assistant will use this tool to create new detections in your local Security Onion instance.
 - **add_overrides**: This tool allows the assistant to tune existing detections by adding overrides to them.
 - **toggle_detections**: The assistant can use this tool to enable or disable existing detections in your local Security Onion instance.
 - **update_detection_content**: If a detection needs its content updated, the assistant can use this tool to update the content and keep the same metadata, overrides, and enabled status.
 - **update_overrides**: This tool allows the assistant to update existing overrides for detections.

Permissions
~~~~~~~~~~~

When the assistant requests any of these tools, the user will be prompted to approve or reject the usage. Approval will have the tool run and the result entered into the conversation followed by a response from the AI. Rejection will notify the assistant and allow it to respond.

Auto Approve Read-Only Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following read-only tools can be used by the assistant without requiring explicit user approval:

 - query_events
 - query_cases
 - query_detections
 - get_playbooks

By default, permission must be granted for each tool request. However, users can enable auto-approval for read-only tools by toggling the slider in the Options dropdown at the top of the assistant page. With the option enabled, read-only tools will auto approve, while tools that modify data will still request explicit user approval.

.. note::

    Conversation data is stored locally and not used to train any models. However, be cautious about sharing sensitive or personal information during your interactions as others in your organization may have access to the conversation history.

Customizing the System Prompt
-----------------------------

The system prompt sets the behavior and context for the AI assistant. Users can customize this prompt to tailor the assistant's responses to their specific needs, such as describing network resources, environments, or workflows. The prompt is included in every session and can be modified at any time on the Administration --> Configuration page under soc --> config --> server --> modules --> assistant --> systemPromptAddendum.

Your system prompt addendum will be added after Security Onion's default system prompt.

.. note::

    Be cautious when customizing the system prompt, as it can significantly influence the assistant's behavior and responses. A longer prompt will also use more credits.

Metrics
-------

Superusers can review token usage and conversation history for all users by going to Administration --> AI Metrics. This page provides usage statistics for a given date range. The page starts with a table of usage by user. Clicking a user's binoculars icon on the right hand side will show any sessions the user interacted with during the selected date range, even deleted sessions. Clicking on a session's binoculars icon will show the full conversation. Administractors can adjust who has permissions via RBAC roles.

To provide an accurate history, deleted sessions are retained on the metrics page even after being deleted by the user.
