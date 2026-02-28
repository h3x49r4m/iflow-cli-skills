# Pipeline Status

**Pipeline:** {{pipeline_name}}
**Feature:** {{feature_name}}
**Started:** {{start_date}}
**Last Updated:** {{last_updated}}

## Current Status

**Phase:** {{current_phase}}/{{total_phases}} - {{current_phase_name}}
**Status:** {{status}}
**Progress:** {{progress_percentage}}%

## Phase Progress

{{#each phases}}
- [{{#if completed}}x{{else}} {{/if}}] Phase {{order}}: {{name}} ({{role}})
  {{#if started_at}}Started: {{started_at}}{{/if}}
  {{#if completed_at}}Completed: {{completed_at}}{{/if}}
  {{#if blocked}}⚠ BLOCKED{{/if}}
{{/each}}

## Active Branches

{{#each branches}}
- **{{name}}** ({{role}})
  - Status: {{status}}
  - Phase: {{phase}}
  - Commits: {{commit_count}}
  {{#if approved_by}}Approved by: {{approved_by}} ({{approved_at}}){{/if}}
{{/each}}

## Skills Used

{{#each skills_used}}
- **{{name}}**: {{version}}
{{/each}}

## Issues

{{#if issues}}
{{#each issues}}
- [{{severity}}] {{title}}
  - Description: {{description}}
  - Assigned to: {{assigned_to}}
  - Status: {{status}}
{{/each}}
{{else}}
No issues reported.
{{/if}}

## Next Steps

1. {{next_step_1}}
2. {{next_step_2}}
3. {{next_step_3}}