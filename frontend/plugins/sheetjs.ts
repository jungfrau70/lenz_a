/* it is safe to import the library from the top level */
import { readFile, utils, set_fs } from 'xlsx';
import { join } from 'path';
import { cwd } from 'process';

export async function getServerSideProps() {
  set_fs(await import("fs")); // dynamically import 'fs' in `getServerSideProps`
  const wb = readFile(join(cwd(), "public", "sheetjs.xlsx"));
  // ...
}