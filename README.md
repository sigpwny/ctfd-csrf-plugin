# ctfd-csrf-plugin

This plugin enables you to fetch the CSRF token for use in a frontend-only theme.

The session nonce is available at `/api/v1/csrf_token`.

## Why is this secure?

- CTFd has CORS on GET endpoints.
- CTFd has CSRF to prevent malicious POST requests.

A malicious site cannot fetch any page on CTFd via a GET request. Thus this endpoint has the same security level as fetching the form page itself.