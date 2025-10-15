from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = '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'

def generate_task_plan(goal_text):
    # Use OpenAI's API to break down the goal into tasks with deadlines and dependencies
    prompt = f"Break down this goal into actionable tasks with suggested deadlines and dependencies: {goal_text}"

    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use different models, e.g., GPT-4 if available
        prompt=prompt,
        max_tokens=500
    )

    return response.choices[0].text.strip()

@app.route('/plan', methods=['POST'])
def create_plan():
    # Get goal from the request body
    goal_text = request.json.get('goal')

    if not goal_text:
        return jsonify({"error": "Goal text is required"}), 400

    # Generate task plan using the LLM
    task_plan = generate_task_plan(goal_text)

    # Return the generated task plan
    return jsonify({"task_plan": task_plan})

if __name__ == '__main__':
    app.run(debug=True)
