# Security Policy

## Supported Versions

`tts-pipeline` is currently pre-alpha. Security fixes will target the default branch until versioned releases begin.

## Reporting A Vulnerability

Please report suspected vulnerabilities privately through GitHub security advisories if available, or by contacting the maintainers through the public organization contact channels.

Do not open a public issue for vulnerabilities involving credentials, provider tokens, private text, generated media, or publishing workflows.

## Secrets And Private Data

Do not commit:

- API keys or provider credentials
- Private text inputs or transcripts
- Generated private audio/video
- OAuth tokens or publishing credentials

Future provider integrations should document what data is sent to external services before they are marked production-ready.
