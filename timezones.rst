UTC and Time Zones
==================

When you run Security Onion Setup, it sets the timezone to UTC/GMT. Logging in UTC is considered a best practice across the cybersecurity industry because it makes it that much easier to correlate events from different systems, organizations, or time zones. Additionally, it avoids with time zones that have daylight savings time which would result in a one-hour time warp twice a year. 

Web interfaces like Kibana should render timestamps in the timezone of your local browser.
