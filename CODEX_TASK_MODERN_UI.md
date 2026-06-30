# AI Haber Portalı - Modern UI Refactoring

## Goal

Transform the current AI News Portal into a modern, clean and responsive news website while preserving ALL existing functionality.

Do NOT rewrite the Python logic.

Only improve the frontend architecture and user interface.

---

# Keep Existing Features

The following features MUST continue working exactly as they do now.

- RSS generated content
- Statistics cards
- Featured news
- Search
- Category filtering
- Archive pages
- Search page
- Navbar
- External news links

---

# New Frontend Architecture

Move inline CSS and JavaScript into separate files.

Create:

outputs/html/
│
├── assets/
│   ├── css/
│   │      news.css
│   ├── js/
│   │      news.js
│   └── images/
│
├── index.html
├── archive.html
└── search.html

Do not leave large <style> or <script> blocks inside HTML.

---

# Visual Style

Use a modern minimal style similar to:

- Stripe
- Linear
- Notion
- Medium
- Microsoft Fluent

Avoid Bootstrap.

Use vanilla CSS.

---

# Colors

Background

#F5F7FA

Cards

#FFFFFF

Primary Blue

#2563EB

Hover Blue

#1D4ED8

Borders

#E5E7EB

Text

#111827

Secondary Text

#6B7280

---

# Typography

Use

font-family:

Segoe UI

fallbacks:

Arial
sans-serif

---

# Layout

Maximum width

1200px

Centered

Large white spaces

Consistent spacing

Responsive

---

# Navbar

Modern sticky navbar.

Contains:

AI News

Current News

Archive

Search

Hover animation

---

# Hero Section

Add a hero section.

Contains:

Title

AI News Portal

Subtitle

Daily AI-powered news summaries generated from RSS feeds.

Search box

Category filters

---

# Search

Large rounded search input.

Search icon.

Placeholder:

Search today's news...

---

# Category Buttons

Rounded pills.

Hover animation.

Active state.

---

# Statistics Cards

Modern cards.

Rounded corners.

Icons.

Large numbers.

Small descriptions.

Shadow.

---

# Featured News

Convert featured news list into cards.

Highlight the most important news.

---

# News Cards

Rounded cards.

Soft shadows.

Hover elevation.

Better spacing.

Category badge.

Source.

Published date.

Read News button.

---

# Footer

Create a modern footer.

Include:

AI News Portal

Generated automatically

RSS Sources

GitHub

Korhan ÖRS

Current year

---

# Responsive

Support

Desktop

Tablet

Mobile

---

# Accessibility

Proper heading hierarchy.

Keyboard navigation.

Visible focus.

---

# Performance

Do not introduce unnecessary JavaScript libraries.

Keep everything lightweight.

---

# Important

Do NOT break existing functionality.

Only improve architecture and design.
