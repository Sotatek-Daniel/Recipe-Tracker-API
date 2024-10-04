# Recipe-Tracker-API

## Migration

- `python manage.py makemigrations --name <change_log> <app_label>`
- `python manage.py migrate`

## Quickstart

- Install postgres, poetry, cmake
- Create .env file with `.env.example` fields
- Run migration:

```
make migrate
```

- Run app:

```
make run
```

## Swagger docs

```
http://localhost:8000/swagger/
```

## Test Serializer

- I create a mork of an Ingredient with the `patch` of `unittest` lib

```
@patch('recipes.serializers.Ingredient.objects.get')
```

- There are 3 test cases:
  - validate ingredient_id
  - valide ingredient_id but not found
  - invalid invalid quantity

## Custom Exception

- I define a base class for APIView. By doing this, I can catch exception globally and prevent unexpected unhanling error to return for the client.
- `Serializer` should raise `APIException`

```
class BaseAPIView(APIView):

    def get_exception_handler(self):
        # default_handler = super().get_exception_handler()

        def handle_exception(exc, context):
            if isinstance(exc, APIException):
                return Response(
                    {
                        'success': False,
                        'code': exc.default_code,
                        'message': exc.default_code,
                    },
                    status=exc.status_code)

            return Response(
                {
                    'success': False,
                    'code': exc.default_code,
                    'message': exc.default_detail,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return handle_exception

```

- Based on the behavior, I can create custom exceptions

```
class IngredientNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Ingredient Not Found.'
    default_code = 'IngredientNotFound'
```

## Further Improvement

- [ ] Dockerfile
- [ ] docker-compose.yaml
