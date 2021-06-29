import utils
import fetch

def test_submission_endpts():
    ids_url, plans_url, cois_url, written_url = utils.submission_endpts("michigan")
    mi_ids = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/beta/submissions/districtr-ids/michigan"
    mi_plan = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/beta/submissions/csv/michigan?type=plan&length=10000"
    mi_cois = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/beta/submissions/csv/michigan?type=coi&length=10000"
    mi_written = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/beta/submissions/csv/michigan?type=written&length=10000"
    assert(ids_url == mi_ids and plans_url == mi_plan and cois_url == mi_cois and written_url == mi_written)
    ids_url, plans_url, cois_url, written_url = utils.submission_endpts("ohio")
    oh_ids = "https://k61e3cz2ni.execute-api.us-east-2.amazonaws.com/prod/submissions/districtr-ids/ohio"
    oh_plan = "https://k61e3cz2ni.execute-api.us-east-2.amazonaws.com/prod/submissions/csv/ohio?type=plan&length=10000"
    oh_cois = "https://k61e3cz2ni.execute-api.us-east-2.amazonaws.com/prod/submissions/csv/ohio?type=coi&length=10000"
    oh_written = "https://k61e3cz2ni.execute-api.us-east-2.amazonaws.com/prod/submissions/csv/ohio?type=written&length=10000"
    assert(ids_url == oh_ids and plans_url == oh_plan and cois_url == oh_cois and written_url == oh_written)

def test_summary_table():
    plans_df, cois_df, written_df = utils.submission_dfs("michigan")
    weeks_1_7_dates = [('2021-5-01', '2021-5-07'), ('2021-5-08', '2021-5-14'), ('2021-5-15', '2021-5-21'), ('2021-5-22', '2021-5-28'), ('2021-5-29', '2021-6-4'), ('2021-6-05', '2021-6-11')]
    weeks_1_7_summary = utils.summary_table(weeks_1_7_dates, plans_df, cois_df, written_df)
    assert(len(weeks_1_7_dates) == len(weeks_1_7_summary))
