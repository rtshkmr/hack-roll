json.extract! question, :id, :question_body, :created_at, :updated_at
json.url question_url(question, format: :json)
