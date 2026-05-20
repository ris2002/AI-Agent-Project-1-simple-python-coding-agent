# AI Agent Project 1 Coding Agent
## Introduction
This project wass coded in reference to to this YouTube video (https://www.youtube.com/watch?v=YtHdaXuOAks&t=414s). The main aim of this project is to learn and understand on the what are AI Agents and how to code them. One slight change is that  I will use Anthropic instead of gemini mentioned in the video. This project for my educational purpose only.
## AI Agents
They are basically LLMs in a loop that use specific tools to complete a task.
LLM (Large Language Models)- They are the reasoning engines
Tools- These are the functions to execute a specific task like scan the directory, search results in internet, code in a specific language, convert text to pdf,translate from one language to another, to ask the user a question whenn in doubt etc.
Loop- AI Agents use these tools in a loop over and over basically they re-prompt over and over again to use the available tools to get a result. The loop will be broken only whe it accomplishes a specific task.

## Example working of AI Agent
Take an example of hypotheical agent that codes a full stack website.
In VS code I activate it and I ask it to code a simple login website.
* It first uses a tool to scan the directory first
* It uses a tool to create frontennd annd backend files and it nnames them accordingly   
* Then it uses a tool to write the code of simple frontend 
* Then it creates a simple database and connects it to the front end
Hence the work is done

## Main diff between in browser LLM and AI Agent 
AI agent has the awareness on what content to work on, not like the browser LLM where we have to copy annd paste
## Features of this Coding Agent
* Scaanns files in directory
* Reads file contents
* Overwrites file contents
* Execute file contents
Repeats these functions until the tasksa are complete 

## Build Understanding 
### Function 1 [get_files_from_wd]
The main use of this function is to check what files are present in the directory 
### Function 2 [get_contents]

### Function 3 [write_file]
### Function 4 
#### Security Risks
Now, it's worth pausing to point out the inherent security risks here. We have a few things going for us:
We'll only allow the LLM to run code in a specific directory (the working_directory).
We'll use a 30-second timeout to prevent it from running indefinitely.
But aside from that... yes, the LLM can run arbitrary code that we place (or it places) in the working directory... so be careful. As long as you use this AI agent only for the simple tasks we're doing in this course, you should be fine. 