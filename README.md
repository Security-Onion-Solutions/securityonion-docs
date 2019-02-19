# securityonion-docs

This repo stores the source code for our documentation which is published by ReadTheDocs at:
https://securityonion.net/docs

We use RST format so that ReadTheDocs can publish both an HTML and PDF format.

# Contributing

If you notice any documentation is missing or incorrect, please feel free to submit a pull request (PR) to this repo.  We will review the PR and merge if appropriate.

# Naming Convention
The end goal of this naming convention is to allow a user to easily guess and type the URL of the documentation they want to go to.

For example, if I want to read more about Suricata, I should be able to type the following into my browser:
https://securityonion.net/docs/suricata

To achieve this goal, new documentation pages should use the following naming convention:
- all lowercase
- .rst file extension
- ideally, the name of the page should be one simple word (for example: suricata.rst)
- try to avoid symbols such as hyphens and underscores
- if symbols are required, hyphens are preferred to underscores
