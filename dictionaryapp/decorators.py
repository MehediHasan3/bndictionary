# decorators.py
from functools import wraps
from .models import SearchLog
from django.utils import timezone

def log_search(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Extract additional information
        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.id

        device_type = request.META.get('DEVICE_TYPE', '')  # You may need to set 'DEVICE_TYPE' in middleware
        browser_info = request.META.get('HTTP_USER_AGENT', '')

        # Measure the time taken for the view to execute
        start_time = timezone.now()
        response = view_func(request, *args, **kwargs)
        end_time = timezone.now()
        search_duration = end_time - start_time

        # Log the request information
        log_entry = SearchLog.objects.create(
            ip=request.META.get('REMOTE_ADDR', ''),
            user_agent=browser_info,
            cookies=str(request.COOKIES),
            query_word='',  # Empty for non-search requests
            location=request.META.get('LOCATION', ''),  # You may need to set 'LOCATION' in middleware
            user_id=user_id,
            device_type=device_type,
            browser_info=browser_info,
            search_duration=search_duration,
            requested_url=request.build_absolute_uri(),  # Log the current URL
        )

        return response

    return _wrapped_view

