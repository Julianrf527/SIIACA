# Apply django.template.context BaseContext copy patch early on import
try:
	from .context_patch import apply_patch
	apply_patch()
except Exception:
	# If patching fails, don't prevent Django from starting; the original
	# error will surface and should be fixed by upgrading/fixing the
	# Django installation.
	pass
