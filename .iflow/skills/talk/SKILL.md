---
name: talk
description: A conversation-only skill for discussing ideas, brainstorming, getting advice, and exploring concepts without any file modifications or system changes
version: 1.0.0
category: conversation
---

# talk

A conversation-only skill for discussing ideas, brainstorming, getting advice, and exploring concepts without any file modifications or system changes.

## Purpose

Pure conversational interaction - talk, discuss, analyze, explore. Nothing gets written or modified.

## Agent Configuration

**Agent Type:** `talk-agent`

**Available Tools:**
- `read_file` - read code/files for discussion
- `glob` - find files to discuss
- `search_file_content` - search to discuss
- `list_directory` - explore structure to discuss
- `web_search` - research for discussion
- `web_fetch` - look up references for discussion
- `image_read` - analyze images for discussion

**Excluded Tools:**
- No file modification tools (write_file, replace, xml_escape)
- No system command tools (run_shell_command)

## Behavior

- Read and analyze for discussion purposes only
- Never write, replace, or run commands
- Pure conversational output: insights, analysis, recommendations

## Usage

When invoked, the agent reads, searches, analyzes, and discusses - nothing gets written to disk.