from rest_framework import viewsets, status
from internal.symbol.models import Symbol
from internal.symbol.serializers import SymbolSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


#Class for CRUD on symbol list
class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer


class SymbolList(APIView):
    def get(self, request):
        symbols = Symbol.objects.all()
        serializer = SymbolSerializer(symbols, many=True)
        return Response(serializer.data)

    def post(self, request):
        symbol_data = request.data.get("symbols", [])
        
        if not symbol_data:
            return Response({"message": "No symbols provided for insertion."}, status=status.HTTP_400_BAD_REQUEST)

        # Deduplicate the provided symbols
        unique_symbols = list(set(symbol_data))

        existing_symbols = Symbol.objects.filter(symbol__in=unique_symbols).values_list('symbol', flat=True)
        new_symbols = [symbol for symbol in unique_symbols if symbol not in existing_symbols]

        if new_symbols:
            # Create new symbols
            new_symbol_objects = [Symbol(symbol=symbol) for symbol in new_symbols]
            Symbol.objects.bulk_create(new_symbol_objects)

        response_data = {
            "new_symbols": new_symbols,
            "existing_symbols": list(existing_symbols)
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        symbols_to_delete = request.data.get('symbols', [])
        if not symbols_to_delete:
            return Response({"message": "No symbols provided for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        symbols_deleted = Symbol.objects.filter(symbol__in=symbols_to_delete).delete()
        return Response({"message": f"{symbols_deleted[0]} symbols deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
