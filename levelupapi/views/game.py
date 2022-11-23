"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game

class GameView(ViewSet):
    """Level up games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            games = Game.objects.get(pk=pk)
            serializer = GameSerializer(games)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        db_cursor.execute("""
            select id, title
            from levelupapi_game
            where id = ?
        """,(pk,)
        )

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()

        # Add in the next 3 lines
        game = request.query_params.get('type', None)
        if game is not None:
            games = games.filter(game_id=game)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

        # select *
        # from levelupapi_game


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Game
        fields = ('id', 'title')
        depth = 1
