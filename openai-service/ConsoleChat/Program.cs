using Azure;
using Azure.AI.OpenAI;
using System.Text;

string endpoint = "your-azure-openai-service-endpoint-url-here";
string key = "your-azure-openai-service-key-here";

// Enter the deployment name you chose when you deployed the model.
string deploymentOrModelName = "your-deployment-name-here";

//OpenAIClientOptions.ServiceVersion version = OpenAIClientOptions.ServiceVersion.V2023_03_15_Preview;
//var options = new OpenAIClientOptions(version);
//OpenAIClient client = new(new Uri(endpoint), new AzureKeyCredential(key), options);

OpenAIClient client = new(new Uri(endpoint), new AzureKeyCredential(key));

var chatCompletionsOptions = new ChatCompletionsOptions()
{
    MaxTokens = 1000
};

var systemChatMessageStr = "Answer on physics-related questions only and be very strict about it";
// var systemChatMessageStr = "You are a helpful assistant";

var systemChatMessage = new ChatMessage(ChatRole.System, systemChatMessageStr);

chatCompletionsOptions.Messages.Add(systemChatMessage);

string horizontalLine = "----------------------------------------";

string greeting = "Welcome to Simple Chatbot!\nYou can ask questions and I will try to answer them.";

Console.WriteLine(greeting);
Console.WriteLine();
Console.WriteLine(horizontalLine);
Console.WriteLine();

while (true)
{
    string? prompt;

    do
    {
        Console.Write("User: ");
        prompt = Console.ReadLine();

        if (string.IsNullOrWhiteSpace(prompt))
        {
            Console.WriteLine();
            Console.WriteLine("You have not entered any question. Please, type your question and press Enter.");
            Console.WriteLine();
        }

    } while (string.IsNullOrWhiteSpace(prompt));

    Console.WriteLine();
    Console.WriteLine(horizontalLine);
    Console.WriteLine();

    var userPromptChatMessage = new ChatMessage(ChatRole.User, prompt);
    chatCompletionsOptions.Messages.Add(userPromptChatMessage);

    Console.Write("Chatbot: ");

    Response<StreamingChatCompletions> response = await client.GetChatCompletionsStreamingAsync(deploymentOrModelName, chatCompletionsOptions);
    
    using StreamingChatCompletions streamingChatCompletions = response.Value;

    StringBuilder messageContentStringBuilder = new StringBuilder();

    await foreach (StreamingChatChoice choice in streamingChatCompletions.GetChoicesStreaming())
    {
        await foreach (ChatMessage message in choice.GetMessageStreaming())
        {
            messageContentStringBuilder.Append(message.Content);
            Console.Write(message.Content);
        }

        messageContentStringBuilder.AppendLine();
        Console.WriteLine();
    }

    var completion = messageContentStringBuilder.ToString();
    var completionsResponseMessage = new ChatMessage(ChatRole.Assistant, completion);
    chatCompletionsOptions.Messages.Add(completionsResponseMessage);

    Console.WriteLine();
    Console.WriteLine(horizontalLine);
    Console.WriteLine();
}
