from transformers import pipeline

# Load text-generation pipeline (uses GPT-2 by default, can be replaced with OpenAI API or other LLMs)
generator = pipeline("text-generation", model="gpt2")

def generate_response(email_body, sentiment, requirements, knowledge_base=None):
    """
    Generate a professional, context-aware response to a support email.
    Optionally uses a knowledge base for Retrieval-Augmented Generation (RAG).
    """
    prompt = (
        "You are a helpful and professional support assistant.\n"
        f"Customer sentiment: {sentiment}\n"
        f"Customer requirements: {requirements}\n"
        f"Email body: {email_body}\n"
    )
    if knowledge_base:
        prompt += f"Relevant knowledge: {knowledge_base}\n"
    prompt += "Draft a friendly, empathetic, and informative reply addressing the customer's needs."

    # Generate response (limit output length for clarity)
    response = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    # Post-process to remove prompt from output if needed
    reply = response.split("Draft a friendly, empathetic, and informative reply addressing the customer's needs.")[-1].strip()
    return reply