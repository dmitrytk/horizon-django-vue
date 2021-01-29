import parse from 'date-fns/parse';
import format from 'date-fns/format';
import differenceInDays from 'date-fns/differenceInDays';
import parseCSV from 'csv-parse/lib/sync';
import EI from './ei';

/**
 * Get data for calculation from csv file
 * @param {String} fileContent
 * @return {Object}
 * */
const parseData = (fileContent) => {
  // const arr = fileContent.trim().split('\n').map((row) => row.split(';'));
  const sheet = parseCSV(fileContent, {
    delimiter: [';', '\t', ','],
    trim: true,
  });
  const km = Number(sheet[1][0]);
  const a = Number(sheet[1][1]);
  const header = sheet[2];
  const body = sheet.slice(3);
  const dates = header.slice(4).map((date) => parse(date, 'dd.MM.yyyy', new Date()));
  const wells = body.map((row) => ({
    name: row[0],
    x: Number(row[1]),
    y: Number(row[2]),
    r: Number(row[3]),
    rates: row.slice(4).map((el) => Number(el)),
    S: [],
  }));
  return {
    km, a, dates, wells,
  };
};

const distance = (well, x, y) => ((well.x - x) ** 2 + (well.y - y) ** 2) ** 0.5;

/**
 * Calculate declines and create header and body for table
 * @param {Object} data
 * @return {Object}
 * */
const calculateDeclineTable = (data) => {
  const header = ['WELL', 'X', 'Y', 'R']
    .concat(data.dates.map((date) => format(date, 'dd.MM.yyyy')));

  for (let i = 0; i < data.dates.length; i += 1) {
    for (let j = 0; j < data.wells.length; j += 1) {
      const well = data.wells[j];
      let SUM = 0;
      for (let k = 1; k < i + 1; k += 1) {
        for (let l = 0; l < data.wells.length; l += 1) {
          const otherWell = data.wells[l];
          const R = well === otherWell ? well.r : distance(well, otherWell.x, otherWell.y);
          const Q = otherWell.rates[k] - otherWell.rates[k - 1];
          const T = differenceInDays(data.dates[i], data.dates[k - 1]);
          const arg = (-R * R) / 4 / data.a / T / 100000;
          SUM += Q * EI(arg);
        }
      }
      const result = -SUM / 4 / 3.14 / data.km;
      well.S.push(Math.round(result * 100) / 100);
    }
  }
  const body = data.wells.map((well) => [well.name, well.x, well.y, well.r].concat(well.S));
  return { header, body };
};

export { parseData, calculateDeclineTable };