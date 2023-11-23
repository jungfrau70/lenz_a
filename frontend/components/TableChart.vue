<script setup>
import { ref, onMounted } from "vue";
import { read, utils, writeFileXLSX } from 'xlsx';

const rows = ref([]);

onMounted(async() => {
  /* Download from https://sheetjs.com/pres.numbers */
  const f = await fetch("https://sheetjs.com/pres.numbers");
  const ab = await f.arrayBuffer();

  /* parse workbook */
  const wb = read(ab);

  /* update data */
  rows.value = utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]]);
});

/* get state data and export to XLSX */
function exportODS() {
  const ws = utils.json_to_sheet(rows.value);
  const wb = utils.book_new();
  utils.book_append_sheet(wb, ws, "Data");
  writeFileXLSX(wb, "SheetJSVueAoO.ods");
}
function exportXLSX() {
  const ws = utils.json_to_sheet(rows.value);
  const wb = utils.book_new();
  utils.book_append_sheet(wb, ws, "Data");
  writeFileXLSX(wb, "SheetJSVueAoO.xlsx");
}
</script>

<template>
  <table><thead><th>Name</th><th>Index</th></thead><tbody>
    <tr v-for="(row, idx) in rows" :key="idx">
      <td>{{ row.Name }}</td>
      <td>{{ row.Index }}</td>
    </tr>
  </tbody><tfoot><td colSpan={2}>
    <button @click="exportXLSX">Export XLSX</button>
    <button @click="exportODS">Export ODS</button>
  </td></tfoot></table>
</template>