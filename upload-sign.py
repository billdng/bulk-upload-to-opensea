# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHRraW50ZXIKaW1wb3J0IHN1YnByb2Nlc3MKZnJvbSB0a2ludGVyIGltcG9ydCAqCmZyb20gdGtpbnRlciBpbXBvcnQgZmlsZWRpYWxvZwppbXBvcnQgdGtpbnRlciBhcyB0awpmcm9tIHRraW50ZXIgaW1wb3J0IG1lc3NhZ2Vib3gKaW1wb3J0IHRraW50ZXIuZm9udCBhcyBmb250CmZyb20gUElMIGltcG9ydCBJbWFnZVRrLCBJbWFnZQppbXBvcnQgdXJsbGliLnJlcXVlc3QKZnJvbSBpbyBpbXBvcnQgQnl0ZXNJTwppbXBvcnQgb3MKaW1wb3J0IGlvCmltcG9ydCBzeXMKaW1wb3J0IHBpY2tsZQppbXBvcnQgdGltZQpmcm9tIGRlY2ltYWwgaW1wb3J0ICoKaW1wb3J0IHdlYmJyb3dzZXIKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydC53YWl0IGltcG9ydCBXZWJEcml2ZXJXYWl0CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQgaW1wb3J0IGV4cGVjdGVkX2NvbmRpdGlvbnMgYXMgRXhwZWN0ZWRDb25kaXRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQudWkgaW1wb3J0IFNlbGVjdAppbXBvcnQganNvbgppbXBvcnQgc3NsCmltcG9ydCBjZXJ0aWZpCgpmcm9tIENTViBpbXBvcnQgQ1NWCmZyb20gSlNPTiBpbXBvcnQgSlNPTgpmcm9tIE5GVCBpbXBvcnQgTkZUCgoKcm9vdCA9IFRrKCkKCnJvb3QuZ2VvbWV0cnkoJzc1MHg3NTAnKQpyb290LnJlc2l6YWJsZShGYWxzZSwgRmFsc2UpCnJvb3QudGl0bGUoIk5GVHMgVXBsb2FkIHRvIE9wZW5TZWEgdjEuMCIpCiAgCmlucHV0X3NhdmVfbGlzdCA9IFsiTkZUcyBmb2xkZXIgOiIsIDAsIDAsIDAsIDAsIDAsIDAsIDAsIDBdCm1haW5fZGlyZWN0b3J5ID0gb3MucGF0aC5qb2luKHN5cy5wYXRoWzBdKQoKCmRlZiBzdXBwb3J0VVJMKCk6CiAgICB3ZWJicm93c2VyLm9wZW5fbmV3KCJodHRwczovL3d3dy5pbmZvdHJleC5uZXQvb3BlbnNlYS9zdXBwb3J0LmFzcD9yPWFwcCIpCgoKY2xhc3MgV2ViSW1hZ2U6CiAgICBkZWYgX19pbml0X18oc2VsZiwgdXJsKToKICAgICAgICB3aXRoIHVybGxpYi5yZXF1ZXN0LnVybG9wZW4odXJsLCBjb250ZXh0PXNzbC5jcmVhdGVfZGVmYXVsdF9jb250ZXh0KGNhZmlsZT1jZXJ0aWZpLndoZXJlKCkpKSBhcyB1OgogICAgICAgICAgICByYXdfZGF0YSA9IHUucmVhZCgpCiAgICAgICAgI3NlbGYuaW1hZ2UgPSB0ay5QaG90b0ltYWdlKGRhdGE9YmFzZTY0LmVuY29kZWJ5dGVzKHJhd19kYXRhKSkKICAgICAgICBpbWFnZSA9IEltYWdlLm9wZW4oaW8uQnl0ZXNJTyhyYXdfZGF0YSkpCiAgICAgICAgc2VsZi5pbWFnZSA9IEltYWdlVGsuUGhvdG9JbWFnZShpbWFnZSkKCiAgICBkZWYgZ2V0KHNlbGYpOgogICAgICAgIHJldHVybiBzZWxmLmltYWdlCmltYWdldXJsID0gImh0dHBzOi8vd3d3LmluZm90cmV4Lm5ldC9vcGVuc2VhL2hlYWRlci5wbmciCmltZyA9IFdlYkltYWdlKGltYWdldXJsKS5nZXQoKQppbWFnZWxhYiA9IHRrLkxhYmVsKHJvb3QsIGltYWdlPWltZykKaW1hZ2VsYWIuZ3JpZChyb3c9MCwgY29sdW1uc3Bhbj0yKQppbWFnZWxhYi5iaW5kKCI8QnV0dG9uLTE+IiwgbGFtYmRhIGU6c3VwcG9ydFVSTCgpKQoKaXNfcG9seWdvbiA9IEJvb2xlYW5WYXIoKQppc19wb2x5Z29uLnNldChGYWxzZSkgCgpkZWYgb3Blbl9jaHJvbWVfcHJvZmlsZSgpOgogICAgc3VicHJvY2Vzcy5Qb3BlbigKICAgICAgICBbCiAgICAgICAgICAgICJzdGFydCIsCiAgICAgICAgICAgICJjaHJvbWUiLAogICAgICAgICAgICAiLS1yZW1vdGUtZGVidWdnaW5nLXBvcnQ9ODk4OSIsCiAgICAgICAgICAgICItLXVzZXItZGF0YS1kaXI9IiArIG1haW5fZGlyZWN0b3J5ICsgIi9jaHJvbWVfcHJvZmlsZSIsCiAgICAgICAgXSwKICAgICAgICBzaGVsbD1UcnVlLAogICAgKQoKCmRlZiBzYXZlX2ZpbGVfcGF0aCgpOgogICAgI3JldHVybiBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0sICJTYXZlX2ZpbGUuY2xvdWQiKSAKICAgIHJldHVybiBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0sICJTYXZlX2d1aS5jbG91ZCIpIAoKCiMgYXNrIGZvciBkaXJlY3Rvcnkgb24gY2xpY2tpbmcgYnV0dG9uLCBjaGFuZ2VzIGJ1dHRvbiBuYW1lLgpkZWYgdXBsb2FkX2ZvbGRlcl9pbnB1dCgpOgogICAgZ2xvYmFsIHVwbG9hZF9wYXRoCiAgICB1cGxvYWRfcGF0aCA9IGZpbGVkaWFsb2cuYXNrZGlyZWN0b3J5KCkKICAgIE5hbWVfY2hhbmdlX2ltZ19mb2xkZXJfYnV0dG9uKHVwbG9hZF9wYXRoKQoKZGVmIE5hbWVfY2hhbmdlX2ltZ19mb2xkZXJfYnV0dG9uKHVwbG9hZF9mb2xkZXJfaW5wdXQpOgogICAgdXBsb2FkX2ZvbGRlcl9pbnB1dF9idXR0b25bInRleHQiXSA9IHVwbG9hZF9mb2xkZXJfaW5wdXQKCmRlZiBpc19udW1lcmljKHZhbCk6CglpZiBzdHIodmFsKS5pc2RpZ2l0KCk6CgkJcmV0dXJuIFRydWUKCWVsaWYgc3RyKHZhbCkucmVwbGFjZSgnLicsJycsMSkuaXNkaWdpdCgpOgoJCXJldHVybiBUcnVlCgllbHNlOgoJCXJldHVybiBGYWxzZQoKY2xhc3MgSW5wdXRGaWVsZDoKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBsYWJlbCwgcm93X2lvLCBjb2x1bW5faW8sIHBvcywgIG1hc3Rlcj1yb290KToKICAgICAgICBzZWxmLm1hc3RlciA9IG1hc3RlcgogICAgICAgIHNlbGYuaW5wdXRfZmllbGQgPSBFbnRyeShzZWxmLm1hc3Rlciwgd2lkdGg9NjApCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5ncmlkKGlwYWR5PTMpCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5sYWJlbCA9IExhYmVsKG1hc3RlciwgdGV4dD1sYWJlbCwgYW5jaG9yPSJ3Iiwgd2lkdGg9MjAsIGhlaWdodD0xICkKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmxhYmVsLmdyaWQocm93PXJvd19pbywgY29sdW1uPWNvbHVtbl9pbywgcGFkeD0xMiwgcGFkeT0yKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQuZ3JpZChyb3c9cm93X2lvLCBjb2x1bW49Y29sdW1uX2lvICsgMSwgcGFkeD0xMiwgcGFkeT0yKQogICAgICAgIHRyeToKICAgICAgICAgICAgd2l0aCBvcGVuKHNhdmVfZmlsZV9wYXRoKCksICJyYiIpIGFzIGluZmlsZToKICAgICAgICAgICAgICAgIG5ld19kaWN0ID0gcGlja2xlLmxvYWQoaW5maWxlKQogICAgICAgICAgICAgICAgc2VsZi5pbnNlcnRfdGV4dChuZXdfZGljdFtwb3NdKQogICAgICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjoKICAgICAgICAgICAgcGFzcwogICAgICAgIAogICAgZGVmIGluc2VydF90ZXh0KHNlbGYsIHRleHQpOgogICAgICAgIHNlbGYuaW5wdXRfZmllbGQuZGVsZXRlKDAsICJlbmQiKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQuaW5zZXJ0KDAsIHRleHQpCgogICAgZGVmIHNhdmVfaW5wdXRzKHNlbGYsIHBvcyk6CiAgICAgICAgI21lc3NhZ2Vib3guc2hvd3dhcm5pbmcoInNob3d3YXJuaW5nIiwgIldhcm5pbmciKQogICAgICAgIGlucHV0X3NhdmVfbGlzdC5pbnNlcnQocG9zLCBzZWxmLmlucHV0X2ZpZWxkLmdldCgpKQogICAgICAgIHdpdGggb3BlbihzYXZlX2ZpbGVfcGF0aCgpLCAid2IiKSBhcyBvdXRmaWxlOgogICAgICAgICAgICBwaWNrbGUuZHVtcChpbnB1dF9zYXZlX2xpc3QsIG91dGZpbGUpCiAgICAgICAgICAgIAogICAg'
love = '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'
god = 'KToKICAgICAgICB3YWl0LnVudGlsKAogICAgICAgICAgICBFeHBlY3RlZENvbmRpdGlvbnMuZWxlbWVudFRvQmVDbGlja2FibGUoKEJ5LkNTU19TRUxFQ1RPUiwgY29kZSkpCiAgICAgICAgKSAgICAKCiAgICBkZWYgd2FpdF94cGF0aChjb2RlKToKICAgICAgICB3YWl0LnVudGlsKEV4cGVjdGVkQ29uZGl0aW9ucy5wcmVzZW5jZV9vZl9lbGVtZW50X2xvY2F0ZWQoKEJ5LlhQQVRILCBjb2RlKSkpCgoKICAgIHdoaWxlIGVuZF9udW0gPj0gc3RhcnRfbnVtOgogICAgICAgIHByaW50KCJTdGFydCBjcmVhdGluZyBORlQgIiArICBsb29wX3RpdGxlICsgc3RyKHN0YXJ0X251bSkpCiAgICAgICAgcHJpbnQoJ251bWJlciAnLCAgc3RhcnRfbnVtKQogICAgICAgIGRyaXZlci5nZXQoY29sbGVjdGlvbl9saW5rKQoKICAgICAgICB3YWl0X3hwYXRoKCcvLypbQGlkPSJtZWRpYSJdJykKICAgICAgICBpbWFnZVVwbG9hZCA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9Im1lZGlhIl0nKQogICAgICAgIGltYWdlUGF0aCA9IG9zLnBhdGguYWJzcGF0aChmaWxlX3BhdGggKyAiXFxpbWFnZXNcXCIgKyBzdHIoc3RhcnRfbnVtKSArICIuIiArIGxvb3BfZmlsZV9mb3JtYXQpICAjIGNoYW5nZSBmb2xkZXIgaGVyZQogICAgICAgIGltYWdlVXBsb2FkLnNlbmRfa2V5cyhpbWFnZVBhdGgpCiAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICBuYW1lID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0ibmFtZSJdJykKICAgICAgICBuYW1lLnNlbmRfa2V5cyhsb29wX3RpdGxlICsgc3RyKHN0YXJ0X251bSkpICAjICsxMDAwIGZvciBvdGhlciBmb2xkZXJzICNjaGFuZ2UgbmFtZSBiZWZvcmUgIiMiCiAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICBleHRfbGluayA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9ImV4dGVybmFsX2xpbmsiXScpCiAgICAgICAgZXh0X2xpbmsuc2VuZF9rZXlzKGxvb3BfZXh0ZXJuYWxfbGluaykKICAgICAgICB0aW1lLnNsZWVwKDIpCgogICAgICAgIGRlc2MgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvLypbQGlkPSJkZXNjcmlwdGlvbiJdJykKICAgICAgICBkZXNjLnNlbmRfa2V5cyhsb29wX2Rlc2NyaXB0aW9uKQogICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgI2pzb25EYXRhID0gSlNPTihmaWxlX3BhdGggKyAiL2pzb24vIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkRnJvbUZpbGUoKQoKICAgICAgICBqc29uRmlsZSA9IGZpbGVfcGF0aCArICIvanNvbi8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIKICAgICAgICBpZiBvcy5wYXRoLmlzZmlsZShqc29uRmlsZSkgYW5kIG9zLmFjY2Vzcyhqc29uRmlsZSwgb3MuUl9PSyk6CiAgICAgICAgICAgCiAgICAgICAgICAgICNwcmludChzdHIoanNvbk1ldGFEYXRhKSkKICAgICAgICAgICAgd2FpdF9jc3Nfc2VsZWN0b3IoImJ1dHRvblthcmlhLWxhYmVsPSdBZGQgcHJvcGVydGllcyddIikKICAgICAgICAgICAgcHJvcGVydGllcyA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfY3NzX3NlbGVjdG9yKCJidXR0b25bYXJpYS1sYWJlbD0nQWRkIHByb3BlcnRpZXMnXSIpCiAgICAgICAgICAgIGRyaXZlci5leGVjdXRlX3NjcmlwdCgiYXJndW1lbnRzWzBdLmNsaWNrKCk7IiwgcHJvcGVydGllcykKICAgICAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAgICAgIyBqc29uRGF0YSA9IEpTT04ob3MuZ2V0Y3dkKCkgKyAiL2RhdGEvIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkRnJvbUZpbGUoKQogICAgICAgICAgICAjIGpzb25NZXRhRGF0YSA9IGpzb25EYXRhWydhdHRyaWJ1dGVzJ10KCiAgICAgICAgICAgICAjIGNoZWNrcyBpZiBmaWxlIGV4aXN0cwogICAgICAgICAgICBqc29uRGF0YSA9IGpzb24ubG9hZHMob3BlbihmaWxlX3BhdGggICsgIlxcanNvblxcIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkKCkpCiAgICAgICAgICAgIGpzb25NZXRhRGF0YSA9IGpzb25EYXRhWydhdHRyaWJ1dGVzJ10KCiAgICAgICAgICAgIGZvciBrZXkgaW4ganNvbk1ldGFEYXRhOgogICAgICAgICAgICAgICAgaW5wdXQxID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy90Ym9keVtAY2xhc3M9IkFzc2V0VHJhaXRzRm9ybS0tYm9keSJdL3RyW2xhc3QoKV0vdGRbMV0vZGl2L2Rpdi9pbnB1dCcpCiAgICAgICAgICAgICAgICBpbnB1dDIgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvL3Rib2R5W0BjbGFzcz0iQXNzZXRUcmFpdHNGb3JtLS1ib2R5Il0vdHJbbGFzdCgpXS90ZFsyXS9kaXYvZGl2L2lucHV0JykKICAgICAgICAgICAgICAgICNwcmludChzdHIoa2V5Wyd0cmFpdF90eXBlJ10pKQogICAgICAgICAgICAgICAgI3ByaW50KHN0cihrZXlbJ3ZhbHVlJ10pKQogICAgICAgICAgICAgICAgaW5wdXQxLnNlbmRfa2V5cyhzdHIoa2V5Wyd0cmFpdF90eXBlJ10pKQogICAgICAgICAgICAgICAgaW5wdXQyLnNlbmRfa2V5cyhzdHIoa2V5Wyd2YWx1ZSddKSkKICAgICAgICAgICAgICAgIGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vYnV0dG9uW3RleHQoKT0iQWRkIG1vcmUiXScpLmNsaWNrKCkKICAgICAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAgICAgZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy9idXR0b25bdGV4dCgpPSJTYXZlIl0nKS5jbGljaygpCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgIyBTZWxlY3QgUG9seWdvbiBibG9ja2NoYWluIGlmIGFwcGxpY2FibGUKICAgICAgICBpZiBpc19wb2x5Z29uLmdldCgpOgogICAgICAgICAgICBibG9ja2NoYWluX2J1dHRvbiA9IGRyaXZlci5maW5kX2VsZW1lbnQoQnkuWFBBVEgsICcvLypbQGlkPSJfX25leHQiXS9kaXZbMV0vbWFpbi9kaXYvZGl2L3NlY3Rpb24vZGl2L2Zvcm0vZGl2WzddL2Rpdi9kaXZbMl0nKQogICAgICAgICAgICBibG9ja2NoYWluX2J1dHRvbi5jbGljaygpCiAgICAgICAgICAgIHBvbHlnb25fYnV0dG9uX2xvY2F0aW9uID0gJy8vc3Bhbltub3JtYWxpemUtc3BhY2UoKSA9ICJNdW1iYWkiXScKICAgICAgICAgICAgd2FpdC51bnRpbChFeHBlY3RlZENvbmRpdGlvbnMucHJlc2VuY2Vfb2ZfZWxlbWVudF9sb2NhdGVkKAogICAgICAgICAgICAgICAgKEJ5LlhQQVRILCBwb2x5Z29uX2J1dHRvbl9sb2NhdGlvbikpKQogICAgICAgICAgICBwb2x5Z29uX2J1dHRvbiA9IGRyaXZlci5maW5kX2VsZW1lbnQoCiAgICAgICAgICAgICAgICBCeS5YUEFUSCwgcG9seWdvbl9idXR0b25fbG9jYXRpb24pCiAgICAgICAgICAgIHBvbHlnb25fYnV0dG9uLmNsaWNrKCkKCgogICAgICAgIGNyZWF0ZSA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9Il9fbmV4dCJdL2RpdlsxXS9tYWluL2Rpdi9kaXYvc2VjdGlvbi9kaXZbMl0vZm9ybS9kaXYvZGl2WzFdL3NwYW4vYnV0dG9uJykKICAgICAgICBkcml2ZXIuZXhlY3V0ZV9zY3JpcHQoImFyZ3VtZW50c1swXS5jbGljaygpOyIsIGNyZWF0ZSkKICAgICAgICB0aW1lLnNsZWVwKDEpCgogICAgICAgIHdhaXRfY3NzX3NlbGVjdG9yKCJpW2FyaWEtbGFiZWw9J0Nsb3NlJ10iKQogICAgICAgIGNyb3NzID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV9jc3Nfc2VsZWN0b3Io'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))