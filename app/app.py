from flask import Flask

app = Flask(__name__)


@app.after_request
def add_security_headers(response):
    # Prevent clickjacking
    response.headers["X-Frame-Options"] = "DENY"

    # Prevent MIME-type sniffing
    response.headers["X-Content-Type-Options"] = "nosniff"

    # Content Security Policy
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self' data:; "
        "font-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'"
    )

    # Control browser permissions
    response.headers["Permissions-Policy"] = (
        "geolocation=(), microphone=(), camera=()"
    )

    # Prevent cross-origin resource embedding
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"

    # Prevent unnecessary caching of application responses
    response.headers["Cache-Control"] = "no-store"

    # Control referrer information
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    return response


@app.route("/")
def home():
    return "DevSecOps Security Pipeline is running!"


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)