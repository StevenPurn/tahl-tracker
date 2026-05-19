---
layout: default
title: "Latest News"
---

<div class="max-w-4xl mx-auto">
  <div class="mb-8 pb-4 border-b border-gray-200 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
    <h2 class="!border-b-0 !pb-0 text-3xl font-black uppercase italic text-gray-800">Latest Game Reports</h2>
    <div class="flex flex-wrap items-center gap-3">
      <span class="text-sm font-bold text-gray-400 uppercase tracking-widest">View by:</span>
      <a href="divisions.html" class="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg text-sm font-bold hover:bg-gray-200 transition-colors uppercase tracking-tight">
        Divisions
      </a>
      <a href="date.html" class="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg text-sm font-bold hover:bg-gray-200 transition-colors uppercase tracking-tight">
        Date
      </a>
      <a href="teams.html" class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-bold hover:bg-blue-700 transition-colors uppercase tracking-tight">
        Team
      </a>
    </div>
  </div>

  <div class="grid gap-6">
    {% for post in site.posts limit:10 %}
      <a href="{{ post.url | relative_url }}" class="group bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-md transition-shadow">
        <div class="p-6">
          <div class="flex items-center justify-between mb-3 text-xs font-bold tracking-widest text-blue-600 uppercase">
            <span>{{ post.division | default: "Adult League" }}</span>
            <span class="text-gray-400">{{ post.date | date: "%B %d, %Y" }}</span>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">
            {{ post.title }}
          </h3>
        </div>
      </a>
    {% else %}
      <div class="text-center py-20 bg-white rounded-2xl border-2 border-dashed border-gray-200">
        <p class="text-gray-400 font-medium italic">No articles found. Sync the server to generate reports!</p>
      </div>
    {% endfor %}
  </div>
</div>