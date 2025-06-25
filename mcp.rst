.. _mcp:

MCP Server
==========

Enterprise customers utilizing their own AI/LLM platform can now interface that platform directly to their Security Onion grid by utilizing the Security Onion Model Context Protocol (MCP) server.

The MCP server gives AI the ability to query alerts, playbooks, events, etc. which provides the LLM with additional information needed to make informed decisions.

.. note::

    The MCP server utilizes the Security Onion Connect API, which is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonion.com/pro for more information about purchasing a Security Onion Pro license to enable this feature.

Configuration
-------------

The MCP server is a low-overhead server application that is maintained separately from the Security Onion software. It's available in a GitHub repository, which includes the installation and configuration instructions.

See https://github.com/Security-Onion-Solutions/securityonion-mcp to get started.

.. note::

    A Connect API Client must be created in the Security Onion API Clients screen. The API Client should be granted sufficient permissions needed to perform the tasks that the LLM will need to execute. 

    For example, if the LLM will be querying events and playbooks then the API Client will need *events/read*, *playbooks/read*, and *detections/read* permissions.

Capabilities
------------

As of 2.4.160, the MCP server currently supports the following operations:

- Query Events via Onion Query Language (OQL)
- Query Playbooks

Future releases will likely bring more functionality, such as the ability to acknowledge alerts.