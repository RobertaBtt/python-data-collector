
schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "job_latitude": {"type": "string"},
    "fleet_email": {"type": "string"},
    "job_id": { "type": "string"},
    "job_state": {"type": "string" },
    "has_delivery": {"type": "string"},
    "job_pickup_latitude": {"type": "string"},
    "job_pickup_name": {"type": "string"},
    "job_status": {"type": "string"},
    "sign_image": {"type": "string"},
    "customer_username": {"type": "string"},
    "job_longitude": {"type": "string"},
    "job_pickup_longitude": {"type": "string"},
    "total_distance_travelled": {"type": "string"},
    "total_time_spent_at_task_till_completion": {"type": "string"},
    "has_pickup": {"type": "string"},
    "job_token": {"type": "string"},
    "job_pickup_address": {"type": "string"},
    "job_pickup_phone": {"type": "string"},
    "fleet_id": {"type": "string"},
    "fleet_name": {"type": "string"},
    "job_pickup_email": {"type": "string"},
    "task_history": {"type": "array",
         "items": [
        {
          "type": "object",
          "properties": {
            "id": {"type": "integer"},
            "job_id": {"type": "integer"},
            "fleet_id": {"type": "integer"},
            "fleet_name": {"type": "string"},
            "latitude": {"type": "string"},
            "longitude": {"type": "string"},
            "type": {"type": "string"},
            "description": {"type": "string"},
            "creation_datetime": {"type": "string"}
          },
          "required": [
            "id",
            "job_id",
            "fleet_id",
            "fleet_name",
            "latitude",
            "longitude",
            "type",
            "description",
            "creation_datetime"
          ]
        }
      ]
    },
    "transaction_fields": {
      "type": "object",
      "properties": {
        "fare_amount": {"type": "number"},
        "driver_amount": {"type": "number"},
        "added_fees": {"type": "integer"}
      },
      "required": [
        "fare_amount",
        "driver_amount",
        "added_fees"
      ]
    }
  },
  "required": [
    "job_latitude",
    "fleet_email",
    "job_id",
    "job_state",
    "has_delivery",
    "job_pickup_latitude",
    "job_pickup_name",
    "job_status",
    "sign_image",
    "customer_username",
    "job_longitude",
    "job_pickup_longitude",
    "total_distance_travelled",
    "total_time_spent_at_task_till_completion",
    "has_pickup",
    "job_token",
    "job_pickup_address",
    "job_pickup_phone",
    "fleet_id",
    "fleet_name",
    "job_pickup_email",
    "task_history",
    "transaction_fields"
  ]
}
