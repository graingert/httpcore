from ssl import SSLContext
from typing import Iterator, Tuple, List, Optional, Type
from types import TracebackType


class SyncDispatchInterface:
    """
    The base abstract interface for sending HTTP requests.

    Concete implementations should subclass this class, and implement
    the `request` method.
    """

    def request(
        self,
        method: bytes,
        url: Tuple[bytes, bytes, int, bytes],
        headers: List[Tuple[bytes, bytes]] = None,
        stream: Iterator[bytes] = None,
        timeout: Tuple[
            Optional[float], Optional[float], Optional[float], Optional[float]
        ] = None,
    ) -> Tuple[
        int, bytes, bytes, List[Tuple[bytes, bytes]], Iterator[bytes]
    ]:
        """
        The interface for sending a single HTTP request, and returning a response.

        **Parameters:**

        * **method** - *bytes* The HTTP method, such as `b'GET'`.
        * **url** - *(bytes, bytes, int, bytes)* The URL as a 4-tuple of (scheme, host, port, path).
        * **headers** - *list of (bytes, bytes), optional* Any HTTP headers to send with the request.
        * **stream** - *bytes async iterator, optional*
        * **timeout** - *(float, float, float, float), all optional.* A tuple of timeout values for (read, write, connect, pool acquiry) operations.
        """
        raise NotImplementedError()

    def close(self):
        """
        Close the implementation, which should close any outstanding response streams,
        and any keep alive connections.
        """
        pass

    def __enter__(self) -> "SyncDispatchInterface":
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> None:
        self.close()


class SyncConnectionPool(SyncDispatchInterface):
    """
    A connection pool for making HTTP requests.

    **Parameters:**

    * **ssl_context** - *SSLContext, optional* An SSL context to use for verifying connections.
    * **max_keepalive** - *int, optional* The maximum number of keep alive connections to maintain in the pool.
    * **max_connections** - *int, optional* The maximum number of HTTP connections to allow. Attempting to establish a connection beyond this limit will block for the duration specified in the pool acquiry timeout.
    """

    def __init__(
        self,
        ssl_context: SSLContext = None,
        max_keepalive: int = None,
        max_connections: int = None,
    ):
        pass

    def request(
        self,
        method: bytes,
        url: Tuple[bytes, bytes, int, bytes],
        headers: List[Tuple[bytes, bytes]] = None,
        stream: Iterator[bytes] = None,
        timeout: Tuple[float, float, float, float] = None,
    ) -> Tuple[
        int, bytes, bytes, List[Tuple[bytes, bytes]], Iterator[bytes]
    ]:
        pass

    def close(self):
        pass


class SyncHTTPProxy(SyncDispatchInterface):
    """
    A connection pool for making HTTP requests via an HTTP proxy.

    **Parameters:**

    * **proxy_url** - *(bytes, bytes, int, bytes)* The URL of the proxy service as a 4-tuple of (scheme, host, port, path).
    * **proxy_headers** - *list of (bytes, bytes), optional* An SSL context to use for verifying connections.
    * **proxy_mode** - *str, optional* A proxy mode to operate in. May be "DEFAULT", "FORWARD_ONLY", or "TUNNEL_ONLY".
    * **ssl_context** - *SSLContext, optional* An SSL context to use for verifying connections.
    * **max_keepalive** - *int, optional* The maximum number of keep alive connections to maintain in the pool.
    * **max_connections** - *int, optional* The maximum number of HTTP connections to allow. Attempting to establish a connection beyond this limit will block for the duration specified in the pool acquiry timeout.
    """

    def __init__(
        self,
        proxy_url: Tuple[bytes, bytes, int, bytes],
        proxy_headers: List[Tuple[bytes, bytes]] = None,
        proxy_mode: str = None,
        ssl_context: SSLContext = None,
        max_keepalive: int = None,
        max_connections: int = None,
    ):
        pass

    def request(
        self,
        method: bytes,
        url: Tuple[bytes, bytes, int, bytes],
        headers: List[Tuple[bytes, bytes]] = None,
        stream: Iterator[bytes] = None,
        timeout: Tuple[float, float, float, float] = None,
    ) -> Tuple[
        int, bytes, bytes, List[Tuple[bytes, bytes]], Iterator[bytes]
    ]:
        pass

    def close(self):
        pass