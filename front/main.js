$(function() {
  const dateFormat = 'yyyy-mm-dd';
  const dailyUrl = 'http://localhost:8000/cache/daily/';
  const totalUrl = 'http://localhost:8000/cache/total/';
  const rowsPerPage = 5;
  let next = 0;

  function renderDaily(response) {
    const table = $('#data');
    table.find('tr').remove();
    response.days.forEach(
        i => table.append(`
            <tr>
                <td>${i.conversation_count}</td>
                <td>${i.missed_chat_count}</td>
                <td>${i.visitors_with_conversation_count}</td>
                <td>${i.date}</td>
            </tr>`));
    const pagination = $('#pagination');
    const activePage = Math.round(next / rowsPerPage);
    pagination.find('li').remove();
    for (let page = 0; page < Math.ceil(response.total / rowsPerPage); page++) {
      pagination.append($(`
        <li class="${page === activePage? 'active': 'waves-effect'}"><a>${page + 1}</a></li>
      `).click(selectPage));
    }
  }

  function renderTotal(data) {
    $('#first-card .card-title').text(data.conversation_count);
    $('#second-card .card-title').text(data.missed_chat_count);
    $('#third-card .card-title').text(data.visitors_with_conversation_count);
  }

  function loadDaily() {
    let startDate = $('#start_date').val();
    let endDate = $('#end_date').val();

    $.getJSON(dailyUrl, {
      start_date: startDate,
      end_date: endDate,
      next: next,
    }, renderDaily);
  }

  function loadTotal() {
    let startDate = $('#start_date').val();
    let endDate = $('#end_date').val();

    $.getJSON(totalUrl, {
      start_date: startDate,
      end_date: endDate,
    }, renderTotal);
  }

  function datesUpdated() {
    next = 0;
    loadDaily();
    loadTotal();
  }

  function selectPage() {
    const page = $(this).find('a').text();
    next = rowsPerPage * (page - 1);
    loadDaily();
  }

  function initDates() {
    let common = {
      autoClose: true,
      format: dateFormat,
      setDefaultDate: true,
    };
    M.Datepicker.init($('#start_date'), {
      ...common,
      defaultDate: new Date(2017, 5, 1),
    });
    M.Datepicker.init($('#end_date'), {
      ...common,
      defaultDate: new Date(2017, 6, 15),
    });
    $('#start_date,#end_date').change(datesUpdated);
  }

  initDates();
  datesUpdated();
});
