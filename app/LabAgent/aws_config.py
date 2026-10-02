""" Creating the boto3 client that will connect to AWS with our credentials and return running sessions """

import boto3
from functools import lru_cache

@lru_cache(maxsize=1) # caching only one return value from this function
def get_session() -> boto3.Session:
    """ One shared session for the entire app """

    return boto3.Session(region_name="us-east-1")


@lru_cache(maxsize=None)
def get_client(service_name: str) -> boto3.client: # type: ignore
    """ Return a boto3 client for a given AWS service """

    return get_session().client(service_name=service_name) # type: ignore