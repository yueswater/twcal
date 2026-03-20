from unittest.mock import patch

from click.testing import CliRunner

from twcal.cli import main


class TestNow:
    def test_now(self):
        import datetime

        fake_today = datetime.date(2026, 3, 20)
        runner = CliRunner()
        with patch("twcal.convert.datetime") as mock_dt:
            mock_dt.date.today.return_value = fake_today
            mock_dt.date.side_effect = lambda *args: datetime.date(*args)
            result = runner.invoke(main, ["now"])
        assert result.exit_code == 0
        assert "民國115年3月20日" in result.output


class TestConvert:
    def test_gregorian_to_minguo(self):
        runner = CliRunner()
        result = runner.invoke(main, ["convert", "2026-03-20"])
        assert result.exit_code == 0
        assert "民國115年3月20日" in result.output

    def test_minguo_to_gregorian(self):
        runner = CliRunner()
        result = runner.invoke(main, ["convert", "-g", "115-03-20"])
        assert result.exit_code == 0
        assert "2026-03-20" in result.output

    def test_invalid_date(self):
        runner = CliRunner()
        result = runner.invoke(main, ["convert", "not-a-date"])
        assert result.exit_code != 0
