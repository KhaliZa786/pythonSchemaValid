def schemaListUsers():

    ListUsers = {
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "email": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "avatar": {
                    "type": "string"
                }
            }
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            }
        }
    }
}


    return ListUsers

def schemaSingleUser():

    SingleUser = {
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "email": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "avatar": {
                    "type": "string"
                }
            }
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            }
        }
    }
}

    return SingleUser

def schemaSingleUserNotFound():

    SingleUserNotFound = {
    "type": "object",
    "properties": {}
}

    return SingleUserNotFound

def schemaListResource():

    ListResource = {
    "properties": {
        "page": {
            "type": "integer"
        },
        "per_page": {
            "type": "integer"
        },
        "total": {
            "type": "integer"
        },
        "total_pages": {
            "type": "integer"
        },
        "data": {
            "type": "array"
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            }
        }
    }
    }


    return ListResource

def schemaSingleResource():

    SingleResource = {
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                },
                "year": {
                    "type": "integer"
                },
                "color": {
                    "type": "string"
                },
                "pantone_value": {
                    "type": "string"
                }
            }
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            }
        }
    }
    }

    return SingleResource

def schemaSingleResourceNotFound():

    SingleResourceNotFound = {
    "properties": {}
}

    return SingleResource

def schemaCreate():
    Create = {
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        }
    }
}
    return Create

def schemaUpdate():
    Update = {
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        }
    }
}
    return Update


def schemaUpdate():
    Update = {
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "updatedAt": {
            "type": "string"
        }
    }
}
    return Update

def schemaDelete():
    Delete = {}
    return Delete

def schemaRegisterSuccessful():
    RegisterSuccessful = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "token": {
            "type": "string"
        }
    }
}
    return RegisterSuccessful

def schemaLoginSuccessful():
    LoginSuccessful = {
    "properties": {
        "token": {
            "type": "string"
        }
    }
}
    return LoginSuccessful

def schemaDelayedResponse():
    DelayedResponse = {
    "properties": {
        "page": {
            "type": "integer"
        },
        "per_page": {
            "type": "integer"
        },
        "total": {
            "type": "integer"
        },
        "total_pages": {
            "type": "integer"
        },
        "data": {
            "type": "array"
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            }
        }
    }
}
    return DelaeyedResponse

