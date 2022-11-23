"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import GameType


class GameTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            game_types = GameType.objects.get(pk=pk)
            serializer = GameTypeSerializer(game_types)
            return Response(serializer.data)
        except GameType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        # db_cursor.execute("""
        #     select id, label
        #     from levelupapi_gametype
        #     where id = ?
        # """,(pk,)
        # )

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_types = GameType.objects.all()

        game_type = request.query_params.get('game_types', None)
        if game_type is not None:
            games = games.filter(game_type_id=game_type)
        serializer = GameTypeSerializer(game_types, many=True)
        return Response(serializer.data)

        # select *
        # from levelupapi_gametype


class GameTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = GameType
        fields = ('id', 'label')
        depth = 1
