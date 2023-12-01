// CandlestickChart.js
import React from 'react';
import { ChartCanvas, Chart } from 'react-stockcharts';
import { CandlestickSeries } from 'react-stockcharts/lib/series';
import { XAxis, YAxis } from 'react-stockcharts/lib/axes';
import { discontinuousTimeScaleProvider } from 'react-stockcharts/lib/scale';
import { fitWidth } from 'react-stockcharts/lib/helper';

class CandlestickChart extends React.Component {
  render() {
    const { data: initialData, width, ratio } = this.props;

    const xScaleProvider = discontinuousTimeScaleProvider.inputDateAccessor(
      (d) => new Date(d.date)
    );
    const { data, xScale, xAccessor, displayXAccessor } = xScaleProvider(
      initialData
    );

    return (
      <ChartCanvas
        height={400}
        width={width}
        ratio={ratio}
        margin={{ left: 50, right: 50, top: 10, bottom: 30 }}
        seriesName="MSFT"
        data={data}
        type="hybrid"
        xAccessor={xAccessor}
        displayXAccessor={displayXAccessor}
        xScale={xScale}
      >
        <Chart id={0} yExtents={(d) => [d.high, d.low]}>
          <XAxis axisAt="bottom" orient="bottom" />
          <YAxis axisAt="right" orient="right" ticks={5} />

          <CandlestickSeries />
        </Chart>
      </ChartCanvas>
    );
  }
}

export default fitWidth(CandlestickChart);
