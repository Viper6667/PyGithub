# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import NamedUser

class CommitComment( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def body( self ):
        self.__completeIfNeeded( self.__body )
        return self.__body

    @property
    def commit_id( self ):
        self.__completeIfNeeded( self.__commit_id )
        return self.__commit_id

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def html_url( self ):
        self.__completeIfNeeded( self.__html_url )
        return self.__html_url

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def line( self ):
        self.__completeIfNeeded( self.__line )
        return self.__line

    @property
    def path( self ):
        self.__completeIfNeeded( self.__path )
        return self.__path

    @property
    def position( self ):
        self.__completeIfNeeded( self.__position )
        return self.__position

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    @property
    def user( self ):
        self.__completeIfNeeded( self.__user )
        return self.__user

    def __initAttributes( self ):
        self.__body = None
        self.__commit_id = None
        self.__created_at = None
        self.__html_url = None
        self.__id = None
        self.__line = None
        self.__path = None
        self.__position = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()
        self.__completed = True

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url,
            None,
            None
        )
        self.__useAttributes( result )

    def delete( self ):
        pass

    def edit( self, body ):
        post_parameters = {
            "body": body,
        }
        result = self.__github._dataRequest(
            "PATCH",
            "https://api.github.com/user",
            None,
            post_parameters
        )
        self.__useAttributes( result )

    def __useAttributes( self, attributes ):
        if "body" in attributes:
            self.__body = attributes[ "body" ]
        if "commit_id" in attributes:
            self.__commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "html_url" in attributes:
            self.__html_url = attributes[ "html_url" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "line" in attributes:
            self.__line = attributes[ "line" ]
        if "path" in attributes:
            self.__path = attributes[ "path" ]
        if "position" in attributes:
            self.__position = attributes[ "position" ]
        if "updated_at" in attributes:
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
        if "user" in attributes:
            self.__user = attributes[ "user" ]
