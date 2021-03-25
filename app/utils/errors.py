# Aqui se define los mensajes de error customizados

EMAIL_IN_USE = ({'message': 'El usuario con este email ya existe'}, 409)
UNAUTHORIZED = ({'message': 'La autentificación es requerida para acceder a este recurso'}, 401)
BAD_CREDENTIALS = ({'message': 'Las credenciales son invalidas'}, 401)
FORBIDDEN = ({'message': 'Prohibido el acceso a este recurso'}, 403)
CODE_NOT_VALID = ({'message': 'Se requiere un código válido para restablecer una contraseña'}, 401)
TOO_MANY_REQUESTS = ({'message': 'Demasiadas solicitudes'}, 429)
